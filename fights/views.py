from django.shortcuts import render
from django.views.generic import TemplateView

class FightPageView(TemplateView):
    template_name = "fights.html"