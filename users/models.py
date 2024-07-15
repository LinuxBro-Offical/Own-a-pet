from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_caretaker = models.BooleanField(default=False)
    is_sponsor = models.BooleanField(default=False)