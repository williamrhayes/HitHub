from django.urls import path
from .views import FighterPageView

urlpatterns = [
    path("", FighterPageView.as_view(), name="fighter"),
]