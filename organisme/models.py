# -*- coding: UTF-8 -*-

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django_extensions.db import fields as exfields

class Organisme(models.Model):
    """Une structure référencée sur le site"""
    id = exfields.UUIDField(primary_key=True)
    nom = models.CharField(max_length=254)
    sigle = models.CharField(max_length=24, blank=True)
    adresse = models.CharField(max_length=512)
    code_postal = models.CharField(max_length=5)
    ville = models.CharField(max_length=254)
    telephone = models.CharField(max_length=10, blank=True)
    email = models.EmailField()
    url = models.URLField(blank=True)
    slug = exfields.AutoSlugField(populate_from='nom')
    reseau = models.BooleanField(default=False)
    actif = models.BooleanField(default=True)
    date_creation = exfields.CreationDateTimeField()
    date_modification = exfields.ModificationDateTimeField()
    auteur = models.ForeignKey(User,null=True)

#mots-cles : voir les solutions existantes d'abord
#trouver un field telephone
#logo / thumb

    class Meta:
        abstract = True
        ordering = ['nom']
        verbose_name, verbose_name_plural = "organisme", "organismes"

    def __unicode__(self):
        return "%s" % (self.nom)

    @models.permalink
    def get_absolute_url(self):
        return ('')
