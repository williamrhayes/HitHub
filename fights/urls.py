from django.urls import path
from .views import FightPageView

urlpatterns = [
    path("", FightPageView.as_view(), name="home"),
    path("fights/", FightPageView.as_view(), name="fights")
]