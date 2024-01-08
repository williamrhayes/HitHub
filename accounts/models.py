from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    hitcoin = models.DecimalField(max_digits=100, decimal_places=2, default=1_000.00)