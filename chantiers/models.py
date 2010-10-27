from django.db import models
from taggit.managers import TaggableManager
from positions.fields import PositionField
from crowdsourcing.models import Survey

# Create your models here.
class Chantier(models.Model):
    """(Chantier description)"""
    nom = models.CharField(blank=True, max_length=120)
    slug = models.SlugField()
    description = models.TextField(blank=True)
#   bidon = models.TextField(blank=True)
    gdocs_folder = models.CharField(blank=True, max_length=40)
    gdocs_email = models.CharField(blank=True, max_length=40)
    gdocs_pass = models.CharField(blank=True, max_length=40)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    position = PositionField()
    tags = TaggableManager(blank = True)
    sondages = models.ManyToManyField(Survey, blank = True)

    class Meta:
        ordering = []
        verbose_name, verbose_name_plural = "Chantier", "Chantiers"

    def __unicode__(self):
        return u"Chantier"

    @models.permalink
    def get_absolute_url(self):
        return ('Chantier', [self.id])