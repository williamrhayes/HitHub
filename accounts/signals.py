from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import CustomUser
from fighters.utils import create_fighter
import numpy as np

@receiver(post_save, sender=CustomUser)
def create_fighter_on_user_create(sender, instance, created, **kwargs):
    if created:
        create_fighter(instance)