from django.contrib import admin
from .models import Fighter, Name, SpiritFighter, Cosmetic

# Register your models here.
admin.site.register(Fighter)
admin.site.register(Name)
admin.site.register(Cosmetic)
admin.site.register(SpiritFighter)