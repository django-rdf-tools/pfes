# -*- coding:utf-8 -*-
from django.contrib.auth.models import User
from main.forms import CredisRegistrationForm

def user_created(sender, user, request, **kwargs):
    form = CredisRegistrationForm(request.POST)
    inscrit = User.objects.get(username=form.data["username"])
    inscrit.first_name = form.data["first_name"]
    inscrit.last_name = form.data["last_name"]
    inscrit.save()
    #print "YOUPIE"

from registration.signals import user_registered    
user_registered.connect(user_created)
