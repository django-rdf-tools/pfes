# icons.py by Hangya
# http://djangosnippets.org/snippets/2182/
# Add this to CSS:
# .icon { padding-left: 20px; background-repeat: no-repeat;}
#
# use at least 20px line-height for best experiences
#
# Download icons from http://www.famfamfam.com/lab/icons/silk/
# Upload them to your MEDIA_URL's icons subdirectory.
#
# Template usage:
# {% load icons %}
#
# <a href="/login/" {% icon 'door_in' %}>Login</a>
# <h2 {% icon 'user' %}>{{ user.username }}</h2>
# <p>Please subscribe to our <span {% icon 'feed' %}>RSS feed</span>.</p>
# <ul><li {% listicon 'bullet_picture' %}>Item</li></ul>
# etc.

from django import template
from django.conf import settings

register = template.Library()

#@register.tag
def icon(icon_name):
  return 'class="icon" style="background-image:url('+settings.MEDIA_URL+'/icons/'+icon_name+'.png);"'
register.simple_tag(icon)

#@register.tag
def listicon(icon_name):
  return 'style="list-style-image:url('+settings.MEDIA_URL+'/icons/'+icon_name+'.png);"'
register.simple_tag(listicon)
