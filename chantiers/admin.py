# -*- coding:utf-8 -*-
from django.contrib import admin
from chantiers.models import Chantier

class ChantierAdmin(admin.ModelAdmin):

    list_display = ('nom',)
    ordering = ('position',)

admin.site.register(Chantier,ChantierAdmin)