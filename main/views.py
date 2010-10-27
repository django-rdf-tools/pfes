# -*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from chantiers.models import Chantier

@login_required
def accueil(request):
    liste_chantiers = Chantier.objects.all().order_by('position')
    return render_to_response('index.html',{'liste':liste_chantiers},RequestContext(request))