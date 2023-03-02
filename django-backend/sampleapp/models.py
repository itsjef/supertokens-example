# Create your models here.
# from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class STUser(models.Model):
    id = models.CharField(primary_key=True, max_length=255, editable=False)
    display_name = models.CharField(max_length=255)

    def __str__(self):
        return f"<{self.id}>: {self.display_name}"
