from django.contrib import admin
from .models import Fight, FightDetail, UpcomingFight

# Register your models here.
admin.site.register(UpcomingFight)
admin.site.register(Fight)
admin.site.register(FightDetail)