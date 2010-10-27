# -*- coding:utf-8 -*-
from django.contrib.syndication.feeds import Feed
from django.contrib.comments.models import Comment

class DerniersComm(Feed):
    title = u"Commentaires PFES"
    link = u"/"
    description= u"Tous les commentaires postés sur la plate-forme d’échanges solidaires Auvergne"
    
    def items(self):
        return Comment.objects.all()[:50]