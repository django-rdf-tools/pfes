# -*- coding:utf-8 -*-
import django.conf.global_settings as DEFAULT_SETTINGS

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVER_EMAIL = 'web@credis.org'
DEFAULT_FROM_EMAIL = 'web@credis.org'

ADMINS = (
    ('CREDIS', 'web@credis.org'),
)
MANAGERS = ADMINS

#acces PGSQL et SMTP dans settings.py

CACHE_BACKEND =	'memcached://127.0.0.1:11211'
CACHE_MIDDLEWARE_SECONDS = 60 *	5
CACHE_MIDDLEWARE_KEY_PREFIX = 'cds' #prefixe pour credis                  
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'fr-FR'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
LOGIN_REDIRECT_URL = '/index.html'

DEFAULT_CONTENT_TYPE = 'text/html'
DEFAULT_CHARSET='utf-8'

MEDIA_ROOT = '/home/admin/domains/credis.org/pfes/media/'
MEDIA_URL = 'http://pfes.credis.org/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = '*vg5gf$*p)v0iy)e&eq2crig$w1&94o8g4cd)=lf2k4m#c_bd='

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'main.context_processors.site_info',
    'main.context_processors.quelchantier',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'pfes.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" 
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/admin/domains/credis.org/pfes/templates'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.comments',
    'django.contrib.gis',
    'django_extensions',
    'rssplug',
    'registration',
    'invitation', #intégré au projet
    'positions',
    'organisme',
    'sorl',
    'crowdsourcing',#intégré au projet
    'taggit',
    'chantiers',
    'south',
    'main',
    'local',
)


#APPS settings
#registration
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_OPEN = True

#invitation
INVITE_MODE = True
ACCOUNT_INVITATION_DAYS = 30
INVITATIONS_PER_USER = 5

#crowdsourcing
CROWDSOURCING_GOOGLE_MAPS_API_KEY = 'ABQIAAAANwNil1jri5II7aYo0xNswBQ3je0CxqZkTzoIK6rPGDfMyj1Z5hT5CRcnY5Lb_oyAhNzOP3n86IZ93g'
#CROWDSOURCING_EXTRA_THUMBNAILS = {'slideshow': {'size': (620, 350)}}

