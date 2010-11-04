# -*- coding:utf-8 -*-
#source http://djangosnippets.org/snippets/1197/
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

def site_info(request):
    site_info = {'protocol': request.is_secure() and 'https' or 'http'}
    if Site._meta.installed:
        site_info['domain'] = Site.objects.get_current().domain
        site_info['name'] = Site.objects.get_current().name
    else:
        site_info['domain'] = RequestSite(request).domain
        site_info['name'] = RequestSite(request).name
    site_info['root'] = site_info['protocol'] + '://' + site_info['domain']
    return site_info

#uniquement si crowdsourcing + chantiers
def quelchantier(request):
    from chantiers.models import Chantier
    from crowdsourcing.models import Survey
    from django.template.defaultfilters import first
    """Pour savoir sur quel chantier on est"""
    mypath = request.path.split("/")
    if mypath[1] == 'sondages': 
        chantier = first(Chantier.objects.filter(sondages__slug = mypath[2]))
        clink = '<a href="/chantiers/'+chantier.slug+'/">'+chantier.nom+'</a>'
        return {'id_chantier': clink }
    else:
        return {'id_chantier': 'false' }