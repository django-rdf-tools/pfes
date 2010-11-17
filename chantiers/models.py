# -*- coding:utf-8 -*-
from django.db import models
from taggit.managers import TaggableManager
from positions.fields import PositionField
from crowdsourcing.models import Survey
from django_extensions.db import fields as exfields

# Create your models here.
class Chantier(models.Model):
    """(Chantier description)"""
    nom = models.CharField(blank=True, max_length=120)
    slug = exfields.AutoSlugField(populate_from='nom')
    description = models.TextField(blank=True)
    gdocs_folder = models.CharField(blank=True, max_length=40)
    gdocs_email = models.CharField(blank=True, max_length=40)
    gdocs_pass = models.CharField(blank=True, max_length=40)
    date_creation = exfields.CreationDateTimeField()
    date_modification = exfields.ModificationDateTimeField()
    position = PositionField()
#   tags = TaggableManager(blank=True)
    sondages = models.ManyToManyField(Survey, blank = True)

    class Meta:
        ordering = []
        verbose_name, verbose_name_plural = "Chantier", "Chantiers"

    def __unicode__(self):
        return u"Chantier"

    @models.permalink
    def get_absolute_url(self):
        return ('Chantier', [self.id])

