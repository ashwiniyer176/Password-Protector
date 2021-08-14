from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
# Create your models here.


class PasswordModel(models.Model):
    websiteLink = models.CharField("Link", max_length=200)
    websiteName = models.CharField("Website Name", max_length=30)
    userName = models.CharField("User Name", max_length=20)
    passwordSaved = models.CharField("Password", max_length=25)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)

    def __str__(self):
        return self.passwordSaved
