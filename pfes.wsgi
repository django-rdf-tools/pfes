ALLDIRS = ['/home/admin/.virtualenvs/credis/lib/python2.6/site-packages']
# the above directory depends on the location of your python installation.
# if using virtualenv, it will need to match your projects locale.
import os
import sys
import site

os.environ["CELERY_LOADER"] = "django"

prev_sys_path = list(sys.path)

for directory in ALLDIRS:
        site.addsitedir(directory)
        new_sys_path = []
        for item in list(sys.path):
                if item not in prev_sys_path:
                        new_sys_path.append(item)
                        sys.path.remove(item)
                        sys.path[:0] = new_sys_path

# change this depending on your project.
sys.path.append('/home/admin/domains/credis.org/')
sys.path.append('/home/admin/domains/credis.org/pfes/')

os.environ['PYTHON_EGG_CACHE'] = '/home/admin/.python-eggs'
os.environ['DJANGO_SETTINGS_MODULE'] = 'pfes.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
