# -*- coding: UTF-8 -*-

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Organisme(models.Model):
    """Une structure référencée sur le site"""
    nom = models.CharField(max_length=254)
    sigle = models.CharField(max_length=24, blank=True)
    adresse = models.CharField(max_length=512)
    code_postal = models.CharField(max_length=5)
    ville = models.CharField(max_length=254)
    telephone = models.CharField(max_length=10, blank=True)
    email = models.EmailField()
    url = models.URLField(blank=True)
    slug = models.SlugField()
    reseau = models.BooleanField(default=False)
    actif = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    auteur = models.ForeignKey(User,null=True)
    relations = models.ManyToManyField("self", through='Relation',symmetrical=False)

#mots-cles : voir les solutions existantes d'abord
#trouver un field telephone
#logo / thumb

    class Meta:
        ordering = ['nom']
        verbose_name, verbose_name_plural = "organisme", "organismes"

    def __unicode__(self):
        return "%s" % (self.nom)

    @models.permalink
    def get_absolute_url(self):
        return ('')

# constantes pour les choix de relations
# voir http://www.b-list.org/weblog/2007/nov/02/handle-choices-right-way/
REL_OCC = 1
REL_REG = 2
REL_PRI = 3

class Relation(models.Model):
    """Une relation entre deux structures"""   
    TYPE_RELATIONS = (
    (REL_OCC, u'Relation occasionnelle'),
    (REL_REG, u'Relation réguliére'),
    (REL_PRI, u'Relation privilégiée'),
    )
    auteur = models.ForeignKey(Organisme, related_name='auteur_related')
    cible = models.ForeignKey(Organisme, related_name='cible_related')
    type = models.PositiveIntegerField(choices=TYPE_RELATIONS)
    datecrea = models.DateTimeField(auto_now_add=True)
    datemodif = models.DateTimeField(auto_now=True)
