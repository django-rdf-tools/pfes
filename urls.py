# -*- coding:utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import *

from django.contrib import admin
admin.autodiscover()
from main.views import *

# pour les RSS
from main.feeds import *
feeds = {
    'comm': DerniersComm,
}

#pour modif formulaire inscription
import main.receivers
from registration.views import register 
from main.forms import CredisRegistrationForm


urlpatterns = patterns('',

    # marche pour local dev only, nginx intercepte sur le serveur
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    # (r'^organisme/', include('pfes.orga.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    
    
    (r'^$', 'main.views.accueil'),
    (r'^index.html$','main.views.accueil'),

    #essai...
    #(r'^chantiers/([-\w]+)/sondages/', include('crowdsourcing.urls')),

    (r'^chantiers/', include('chantiers.urls')),
    (r'^sondages/', include('crowdsourcing.urls')),

    #interception du formulaire par défaut de registration
    (r'^accounts/register/$', register, 
    {'backend': 'registration.backends.credis.DefaultBackend', 
    'form_class':CredisRegistrationForm},
    #name='registration_register'
    ),

    (r'^accounts/', include('invitation.urls')),
    
    (r'^accounts/', include('registration.backends.default.urls')),
   # (r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html',}),
    
    
    
)
