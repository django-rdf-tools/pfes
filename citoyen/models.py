# -*- coding:utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django_extensions.db import fields as exfields


class Profil(models.Model):
    """Profil utilisateur générique"""
    
    id = exfields.UUIDField(primary_key=True)
    user = models.ForeignKey(User, unique=True)
    adresse = models.CharField(blank=True, max_length=100)
    code_postal = models.CharField(max_length=5)
    ville = models.CharField(max_length=254)
    telephone = models.CharField(max_length=10, blank=True)
    date_creation = exfields.CreationDateTimeField()
    date_modification = exfields.ModificationDateTimeField()

    class Meta:
        verbose_name, verbose_name_plural = "profil utilisateur", "profils utilisateur"

    def __unicode__(self):
        return "%s" % (self.user.username)

    @models.permalink
    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
