# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class UserInfo(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    objectguid = models.CharField(max_length=255)
    userprincipalname = models.CharField(max_length=100, blank=True, null=True)
    objectsid = models.CharField(primary_key=True, max_length=255)
    samaccountname = models.CharField(max_length=50)
    enabled = models.BooleanField()
    name = models.CharField(max_length=50)
    adspath = models.CharField(max_length=255)
    canonicalname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'UserInfo'

    def __str__(self):
        return self.samaccountname + ', ' + self.objectsid


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
