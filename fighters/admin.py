from django.contrib import admin
from .models import Fighter, SpiritFighter, Cosmetic

# Register your models here.
admin.site.register(Fighter)
admin.site.register(Cosmetic)
admin.site.register(SpiritFighter)