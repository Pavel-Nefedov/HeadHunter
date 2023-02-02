from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from mainapp.mixins import IsModeratorCheckMixin


@method_decorator(login_required, name='dispatch')
class ModeratorLkIndex(IsModeratorCheckMixin, TemplateView):
    template_name = 'moderatorapp/index.html'


