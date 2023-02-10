from django.http import HttpResponseRedirect
from django.urls import reverse


class IsModeratorCheckMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_moderator:
            return HttpResponseRedirect(reverse('authapp:login'))
        return super().dispatch(request, *args, **kwargs)


class IsCandidateCheckMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_candidate:
            return HttpResponseRedirect(reverse('authapp:login'))
        return super().dispatch(request, *args, **kwargs)

class IsCompanyCheckMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_company:
            return HttpResponseRedirect(reverse('authapp:login'))
        return super().dispatch(request, *args, **kwargs)
