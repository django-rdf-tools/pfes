# Create your views here.
from django.template import RequestContext
from chantiers.models import Chantier
from crowdsourcing.models import Survey
from django.shortcuts import render_to_response
from django.template.defaultfilters import first

#from django.conf import settings
#from django.views.generic.simple import direct_to_template
#from django.core.urlresolvers import reverse
#from django.contrib.auth.decorators import login_required

import gdata.docs.service
import gdata.base.service
import gdata.base
from gdata.client import atom


def index(request):
    liste_chantiers = Chantier.objects.all().order_by('position') 
    for c in liste_chantiers:
        c.nbsondages = c.sondages.count()
    return render_to_response('chantiers/index.html',{'chantiers':liste_chantiers},RequestContext(request))



def detail(request, cslug):
    lechantier = first(Chantier.objects.filter(slug = cslug))
    ledict = {'chantier':lechantier}
    sondages = lechantier.sondages.all()
    ledict['nbsondages'] = sondages.count()
    ledict['sondages'] = sondages
    
    if len(lechantier.gdocs_folder) > 1:
        gd_client = gdata.docs.service.DocsService()
        gd_client = gdata.docs.service.DocsService(source='Quinode-pfes-v1')
        gd_client.ClientLogin(lechantier.gdocs_email, lechantier.gdocs_pass)
        q = gdata.docs.service.DocumentQuery()
        q.AddNamedFolder(lechantier.gdocs_email, lechantier.gdocs_folder)
        feed = gd_client.Query(q.ToUri())
        parsedfeed = []
        for entry in feed.entry:
            doclink = {}
            doclink['title'] = entry.title.text
            doclink['link'] = entry.GetAlternateLink().href
            parsedfeed.append(doclink)
        
        ledict['docs'] = parsedfeed
        
    return render_to_response('chantiers/detail.html', ledict, RequestContext(request))
