from django.urls import path
from .views import BetPageView

urlpatterns = [
    path("", BetPageView.as_view(), name="bet"),
]