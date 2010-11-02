# -*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from chantiers.models import Chantier
from django.contrib.auth.models import User

@login_required
def accueil(request):
    liste_chantiers = Chantier.objects.all().order_by('position') 
    for c in liste_chantiers:
        c.nbsondages = c.sondages.count()
    return render_to_response('index.html',{'chantiers':liste_chantiers},RequestContext(request))
    
@login_required
def utilisateurs(request):
    liste_users = User.objects.all()
    return render_to_response('utilisateurs.html',{'utilisateurs':liste_users},RequestContext(request))
    