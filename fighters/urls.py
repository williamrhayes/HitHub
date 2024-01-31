from django.urls import path
from .views import FighterPageView

urlpatterns = [
    path("", FighterPageView.as_view(), name="fighters"),
    path("cosmetics/", FighterPageView.as_view(), name="cosmetics"),
]