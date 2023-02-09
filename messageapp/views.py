from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from candidateapp.models import Resume
from companyapp.models import Vacancy, CompanyProfile
from mainapp.mixins import IsModeratorCheckMixin
from messageapp.forms import MessageForm
from messageapp.models import Chat, Message


class DialogsView(View):
    def get(self, request):
        chats = Chat.objects.filter(members__in=[request.user.id])
        return render(request, 'messageapp/dialogs.html', {'user_profile': request.user, 'chats': chats})


# Create your views here.


class MessagesView(View):
    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            user_chats = Chat.objects.filter(members__in=[request.user.id])
            interlocutor = chat.members.exclude(id=request.user.id)[0]
            if request.user in chat.members.all():
                chat.message_set.filter(is_readed=False).exclude(author=request.user).update(is_readed=True)
            else:
                chat = None
                interlocutor = None
                user_chats = None
        except Chat.DoesNotExist:
            chat = None
            interlocutor = None
            user_chats = None

        return render(
            request,
            'messageapp/messages.html',
            {
                'user_profile': request.user,
                'chat': chat,
                'user_chats': user_chats,
                'interlocutor': interlocutor,
                'form': MessageForm()
            }
        )

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('messageapp:messages', kwargs={'chat_id': chat_id}))


class CreateDialogView(View):
    def get(self, request, user_id):
        chats = Chat.objects.filter(
            members__in=[request.user.id, user_id], type=Chat.DIALOG
        ).annotate(c=Count('members')).filter(c=2)
        if chats.count() == 0:
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        return redirect(reverse('messageapp:messages', kwargs={'chat_id': chat.id}))


@method_decorator(login_required, name='dispatch')
class ModeratorApproveView(IsModeratorCheckMixin, View):
    RESUME = 'resume'
    VACANCY = 'vacancy'
    COMPANY_PROFILE = 'company_profile'

    ALLOWED_APPROVE_TYPES = [RESUME, VACANCY, COMPANY_PROFILE]

    def get(self, request, user_id, query_set_id, approve_type):
        if approve_type not in self.ALLOWED_APPROVE_TYPES:
            raise Http404('Not allow type for approve.')

        with transaction.atomic():
            chats = Chat.objects.filter(
                members__in=[request.user.id, user_id], type=Chat.DIALOG
            ).annotate(c=Count('members')).filter(c=2)
            if chats.count() == 0:
                chat = Chat.objects.create()
                chat.members.add(request.user)
                chat.members.add(user_id)
            else:
                chat = chats.first()

            if approve_type == self.RESUME:
                # Делаем метку резюме, что оно отмодерировано
                this_qs = Resume.objects.get(pk=query_set_id)
                this_qs.is_moderated = True
                this_qs.save()
                current_message = f"Ваше <a href='{reverse('candidateapp:resume_detail', kwargs={'pk': this_qs.pk})}'>резюме<a> принято модератором."
                redirect_url = reverse('moderator:moderator_lk_resume')

            if approve_type == self.VACANCY:
                # Делаем метку резюме, что оно отмодерировано
                this_qs = Vacancy.objects.get(pk=query_set_id)
                this_qs.is_moderated = True
                this_qs.save()
                current_message = f"Ваша <a href='{reverse('company:vacancy', kwargs={'pk': this_qs.pk})}'>вакансия<a> принята модератором."
                redirect_url = reverse('moderator:moderator_lk_vacancy')

            if approve_type == self.COMPANY_PROFILE:
                # Делаем метку резюме, что оно отмодерировано
                this_qs = CompanyProfile.objects.get(pk=query_set_id)
                this_qs.is_moderated = True
                this_qs.save()
                current_message = f"Ваш  <a href='{reverse('company:company_profile')}'>профиль компании<a> одобрен модератором."
                redirect_url = reverse('moderator:moderator_lk_company_profile')

            # Отправим сообщение пользователю
            Message.objects.create(
                chat=chat,
                author=request.user,
                message=current_message,
            )

        return redirect(redirect_url)


@method_decorator(login_required, name='dispatch')
class ModeratorRejectView(IsModeratorCheckMixin, View):
    RESUME = 'resume'
    VACANCY = 'vacancy'
    COMPANY_PROFILE = 'company_profile'

    ALLOWED_APPROVE_TYPES = [RESUME, VACANCY, COMPANY_PROFILE]

    def get(self, request, user_id, query_set_id, reject_type):
        if reject_type not in self.ALLOWED_APPROVE_TYPES:
            raise Http404('Not allow type for reject.')

        with transaction.atomic():
            chats = Chat.objects.filter(
                members__in=[request.user.id, user_id], type=Chat.DIALOG
            ).annotate(c=Count('members')).filter(c=2)
            if chats.count() == 0:
                chat = Chat.objects.create()
                chat.members.add(request.user)
                chat.members.add(user_id)
            else:
                chat = chats.first()

            reject_reason = ''
            if request.GET['reject_reason']:
                reject_reason = 'Причина отказа: ' + request.GET['reject_reason']

            if reject_type == self.RESUME:
                # Делаем метку резюме, что оно отмодерировано
                this_qs = Resume.objects.get(pk=query_set_id)
                current_message = f"Ваше <a href='{reverse('candidateapp:resume_detail', kwargs={'pk': this_qs.pk})}'>резюме<a> не прошло модерацию. {reject_reason}"
                redirect_url = reverse('moderator:moderator_lk_resume')

            if reject_type == self.VACANCY:
                # Делаем метку резюме, что оно отмодерировано
                this_qs = Vacancy.objects.get(pk=query_set_id)
                current_message = f"Ваша <a href='{reverse('company:vacancy', kwargs={'pk': this_qs.pk})}'>вакансия<a> не прошла модерацию. {reject_reason}"
                redirect_url = reverse('moderator:moderator_lk_vacancy')

            if reject_type == self.COMPANY_PROFILE:
                # Делаем метку резюме, что оно отмодерировано
                this_qs = CompanyProfile.objects.get(pk=query_set_id)
                current_message = f"Ваш  a href='{reverse('company:company_profile')}'>профиль компании<a> не прошел модерацию. {reject_reason}"
                redirect_url = reverse('moderator:moderator_lk_company_profile')

            # Отправим сообщение пользователю
            Message.objects.create(
                chat=chat,
                author=request.user,
                message=current_message,
            )

        return redirect(redirect_url)
