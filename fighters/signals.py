from django.db.models.signals import post_save
from django.dispatch import receiver
from fighters.utils import determine_cosmetic_colors
import numpy as np

@receiver(post_save, sender='fighters.Cosmetic')
def determine_colors_on_cosmetic_create(instance, created, **kwargs):
    if created:
        current_color_data = instance.color_data
        updated_color_data = determine_cosmetic_colors(instance.img)