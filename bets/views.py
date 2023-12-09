from django.shortcuts import render
from django.views.generic import TemplateView

class BetPageView(TemplateView):
    template_name = "bets.html"