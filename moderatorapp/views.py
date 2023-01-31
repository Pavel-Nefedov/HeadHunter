from django.shortcuts import render
from django.views.generic import TemplateView


class ModeratorLkIndex(TemplateView):
    template_name = 'moderatorapp/index.html'
