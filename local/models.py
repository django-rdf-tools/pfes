# -*- coding: UTF-8 -*-
from organisme.models import Organisme
from django.db import models

class OrganismeLocal(Organisme):
    """Les champs complémentaires de ce réseau"""
    fse = models.BooleanField(default=True)
    relations = models.ManyToManyField("self", through='Relation',symmetrical=False)

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
    auteur = models.ForeignKey(OrganismeLocal, related_name='auteur_related')
    cible = models.ForeignKey(OrganismeLocal, related_name='cible_related')
    type_relation = models.PositiveIntegerField(choices=TYPE_RELATIONS)
    date_crea = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

