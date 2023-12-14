from django.shortcuts import render
from django.views.generic import TemplateView

class FighterPageView(TemplateView):
    template_name = "fighters.html"