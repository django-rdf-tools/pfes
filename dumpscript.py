#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# ./manage.py dumpscript

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    def run():

        from django.contrib.auth.models import User

        auth_user_1 = User()
        auth_user_1.username = u'pdelage'
        auth_user_1.first_name = u'Pascal'
        auth_user_1.last_name = u'Delage'
        auth_user_1.email = u'fudoeditions@free.fr'
        auth_user_1.password = u'sha1$c9a1e$fc570680e59c222cca5f41217a7688e864bb2e42'
        auth_user_1.is_staff = False
        auth_user_1.is_active = True
        auth_user_1.is_superuser = False
        auth_user_1.last_login = datetime.datetime(2010, 11, 4, 10, 48, 26, 413453)
        auth_user_1.date_joined = datetime.datetime(2010, 11, 4, 10, 47, 8, 867420)
        auth_user_1.save()

        auth_user_2 = User()
        auth_user_2.username = u'mdigonnet'
        auth_user_2.first_name = u'Marc'
        auth_user_2.last_name = u'Digonnet'
        auth_user_2.email = u'mdigonnet@orange.fr'
        auth_user_2.password = u'sha1$f5905$eaf74b72b690c07769f3a12c864a080cd5e04d72'
        auth_user_2.is_staff = False
        auth_user_2.is_active = True
        auth_user_2.is_superuser = False
        auth_user_2.last_login = datetime.datetime(2010, 11, 2, 23, 24, 35)
        auth_user_2.date_joined = datetime.datetime(2010, 11, 2, 23, 23, 33)
        auth_user_2.save()

        auth_user_3 = User()
        auth_user_3.username = u'lejardindesestreys'
        auth_user_3.first_name = u'Georges'
        auth_user_3.last_name = u'Hantz'
        auth_user_3.email = u'georges.hantz.jde@orange.fr'
        auth_user_3.password = u'sha1$b0c2a$bc37a931b19affce6225c42e95ec8c395a801f83'
        auth_user_3.is_staff = False
        auth_user_3.is_active = True
        auth_user_3.is_superuser = False
        auth_user_3.last_login = datetime.datetime(2010, 11, 3, 22, 2, 21)
        auth_user_3.date_joined = datetime.datetime(2010, 11, 3, 22, 1)
        auth_user_3.save()

        auth_user_4 = User()
        auth_user_4.username = u'Covoiturageauvergne'
        auth_user_4.first_name = u'Mathilde'
        auth_user_4.last_name = u'Deroo'
        auth_user_4.email = u'covoiturageauvergne@orange.fr'
        auth_user_4.password = u'sha1$98778$57185fb0e02cfa5d448224d16aa866b88cc35584'
        auth_user_4.is_staff = False
        auth_user_4.is_active = True
        auth_user_4.is_superuser = False
        auth_user_4.last_login = datetime.datetime(2010, 11, 2, 11, 42, 49)
        auth_user_4.date_joined = datetime.datetime(2010, 11, 2, 11, 39, 30)
        auth_user_4.save()

        auth_user_5 = User()
        auth_user_5.username = u'cotravauxauvergne'
        auth_user_5.first_name = u'Thierry'
        auth_user_5.last_name = u'Keller'
        auth_user_5.email = u'coordination@auvergne.cotravaux.org'
        auth_user_5.password = u'sha1$171fe$a622d6ef0ad7689be66300e8981b85a51438cedc'
        auth_user_5.is_staff = False
        auth_user_5.is_active = True
        auth_user_5.is_superuser = False
        auth_user_5.last_login = datetime.datetime(2010, 10, 11, 13, 58, 45, 4837)
        auth_user_5.date_joined = datetime.datetime(2010, 10, 11, 13, 57, 31, 743759)
        auth_user_5.save()

        auth_user_6 = User()
        auth_user_6.username = u'EmmaPOIX'
        auth_user_6.first_name = u'Emmanuelle'
        auth_user_6.last_name = u'Poix'
        auth_user_6.email = u'emma.poix@wanadoo.fr'
        auth_user_6.password = u'sha1$f828b$5ca10999f01b672b0f8d8f60d7f65a409d008b8b'
        auth_user_6.is_staff = True
        auth_user_6.is_active = True
        auth_user_6.is_superuser = False
        auth_user_6.last_login = datetime.datetime(2010, 11, 2, 10, 50, 5)
        auth_user_6.date_joined = datetime.datetime(2010, 10, 13, 12, 30, 50)
        auth_user_6.save()

        auth_user_7 = User()
        auth_user_7.username = u'Hebrard'
        auth_user_7.first_name = u'Olivier'
        auth_user_7.last_name = u'Hebrard'
        auth_user_7.email = u'olivier.hebrard@gmail.com'
        auth_user_7.password = u'sha1$da3fa$fcca42c8dafad76d7625b73dfd5b039bccbb0b59'
        auth_user_7.is_staff = False
        auth_user_7.is_active = True
        auth_user_7.is_superuser = False
        auth_user_7.last_login = datetime.datetime(2010, 10, 11, 12, 11, 24)
        auth_user_7.date_joined = datetime.datetime(2010, 10, 11, 12, 10, 21)
        auth_user_7.save()

        auth_user_8 = User()
        auth_user_8.username = u'PierreSAUVAT'
        auth_user_8.first_name = u'Pierre'
        auth_user_8.last_name = u'Sauvat'
        auth_user_8.email = u'p.sauvat@gmail.com'
        auth_user_8.password = u'sha1$69c15$c664eb48fc6e04b3395f122813534c1dc047cfaa'
        auth_user_8.is_staff = False
        auth_user_8.is_active = True
        auth_user_8.is_superuser = False
        auth_user_8.last_login = datetime.datetime(2010, 10, 18, 22, 15, 10)
        auth_user_8.date_joined = datetime.datetime(2010, 10, 18, 22, 12, 36)
        auth_user_8.save()

        auth_user_9 = User()
        auth_user_9.username = u'ag'
        auth_user_9.first_name = u'Aurelie'
        auth_user_9.last_name = u'Grenard'
        auth_user_9.email = u'atoutvabien@hotmail.fr'
        auth_user_9.password = u'sha1$9013c$e6f5c222c820fba1e2882b09cf874d0708ba9838'
        auth_user_9.is_staff = False
        auth_user_9.is_active = True
        auth_user_9.is_superuser = False
        auth_user_9.last_login = datetime.datetime(2010, 11, 2, 11, 37, 45)
        auth_user_9.date_joined = datetime.datetime(2010, 11, 2, 11, 37, 9)
        auth_user_9.save()

        auth_user_10 = User()
        auth_user_10.username = u'mguy63'
        auth_user_10.first_name = u'Michel'
        auth_user_10.last_name = u'Guy'
        auth_user_10.email = u'mguy63@gmail.com'
        auth_user_10.password = u'sha1$17b70$73a5f097645036a7eaae94beec2bd54fffed1fb7'
        auth_user_10.is_staff = False
        auth_user_10.is_active = True
        auth_user_10.is_superuser = False
        auth_user_10.last_login = datetime.datetime(2010, 10, 19, 22, 25, 27)
        auth_user_10.date_joined = datetime.datetime(2010, 10, 19, 22, 4, 44)
        auth_user_10.save()

        auth_user_11 = User()
        auth_user_11.username = u'Cyrille'
        auth_user_11.first_name = u'Cyrille'
        auth_user_11.last_name = u'Terrier'
        auth_user_11.email = u'cyrille_terrier@yahoo.fr'
        auth_user_11.password = u'sha1$af1c3$5ece456f12348bb2e102e8708df4af7d073dab9e'
        auth_user_11.is_staff = False
        auth_user_11.is_active = True
        auth_user_11.is_superuser = False
        auth_user_11.last_login = datetime.datetime(2010, 10, 13, 14, 6, 39, 997355)
        auth_user_11.date_joined = datetime.datetime(2010, 10, 13, 14, 6, 4, 680416)
        auth_user_11.save()

        auth_user_12 = User()
        auth_user_12.username = u'bheniau'
        auth_user_12.first_name = u'benoit'
        auth_user_12.last_name = u'Heniau'
        auth_user_12.email = u'b.heniau@orange.fr'
        auth_user_12.password = u'sha1$e0d85$79ebc59c2df9f265ee2a5b933bcd01dee769ec47'
        auth_user_12.is_staff = False
        auth_user_12.is_active = True
        auth_user_12.is_superuser = False
        auth_user_12.last_login = datetime.datetime(2010, 11, 2, 20, 30, 1, 911907)
        auth_user_12.date_joined = datetime.datetime(2010, 11, 2, 20, 28, 28, 818567)
        auth_user_12.save()

        auth_user_13 = User()
        auth_user_13.username = u'sdrouard'
        auth_user_13.first_name = u'Sylviane'
        auth_user_13.last_name = u'Drouard'
        auth_user_13.email = u'sylvianemail@gmail.com'
        auth_user_13.password = u'sha1$5d31e$122425c80589e42a5083e26b4c37c26642ff3e08'
        auth_user_13.is_staff = False
        auth_user_13.is_active = True
        auth_user_13.is_superuser = False
        auth_user_13.last_login = datetime.datetime(2010, 11, 4, 12, 53, 3)
        auth_user_13.date_joined = datetime.datetime(2010, 11, 4, 12, 46, 45)
        auth_user_13.save()

        auth_user_14 = User()
        auth_user_14.username = u'lafont'
        auth_user_14.first_name = u'lafont'
        auth_user_14.last_name = u'pascal'
        auth_user_14.email = u'lesateliersdelabruyere@wanadoo.fr'
        auth_user_14.password = u'sha1$51ec4$e9467db15631873d32e4c2b8230c803bef4dc435'
        auth_user_14.is_staff = False
        auth_user_14.is_active = True
        auth_user_14.is_superuser = False
        auth_user_14.last_login = datetime.datetime(2010, 11, 4, 15, 34, 41, 724009)
        auth_user_14.date_joined = datetime.datetime(2010, 11, 4, 15, 34, 2, 801120)
        auth_user_14.save()

        auth_user_15 = User()
        auth_user_15.username = u'isabellegarderes'
        auth_user_15.first_name = u'Isabelle'
        auth_user_15.last_name = u'Garderes'
        auth_user_15.email = u'isabellegarderes@gmail.com'
        auth_user_15.password = u'sha1$89b69$dfeb218d9787489a185f09dc3da3a3d6773c5aef'
        auth_user_15.is_staff = False
        auth_user_15.is_active = True
        auth_user_15.is_superuser = False
        auth_user_15.last_login = datetime.datetime(2010, 11, 4, 21, 30, 5, 62214)
        auth_user_15.date_joined = datetime.datetime(2010, 11, 4, 21, 29, 23, 917187)
        auth_user_15.save()

        auth_user_16 = User()
        auth_user_16.username = u'admin'
        auth_user_16.first_name = u'Dominique'
        auth_user_16.last_name = u'Guardiola'
        auth_user_16.email = u'contact@quinode.fr'
        auth_user_16.password = u'sha1$2444e$afd8c4a19d61aed69a1141f3232ec9f3465fd060'
        auth_user_16.is_staff = True
        auth_user_16.is_active = True
        auth_user_16.is_superuser = True
        auth_user_16.last_login = datetime.datetime(2010, 11, 4, 21, 46, 6, 565846)
        auth_user_16.date_joined = datetime.datetime(2010, 10, 10, 21, 49, 48)
        auth_user_16.save()

        auth_user_17 = User()
        auth_user_17.username = u'gearkose'
        auth_user_17.first_name = u'Nicole'
        auth_user_17.last_name = u'Pialoux'
        auth_user_17.email = u'ge.arkose@wanadoo.fr'
        auth_user_17.password = u'sha1$dc6ff$57d802a8f15632dd8cf503775c10ebffc7237d99'
        auth_user_17.is_staff = False
        auth_user_17.is_active = True
        auth_user_17.is_superuser = False
        auth_user_17.last_login = datetime.datetime(2010, 11, 2, 21, 13, 47)
        auth_user_17.date_joined = datetime.datetime(2010, 11, 2, 21, 12, 56)
        auth_user_17.save()


        from django.contrib.sites.models import Site

        django_site_1 = Site.objects.get(id=1)
        django_site_1.domain = u'localhost:8000'
        django_site_1.name = u'Plate-forme d\u2019\xe9changes Solidaires'
        django_site_1.save()


        from django.contrib.comments.models import Comment

        django_comments_1 = Comment()
        django_comments_1.content_type = ContentType.objects.get(app_label="crowdsourcing", model="survey")
        django_comments_1.object_pk = u'2'
        django_comments_1.site = django_site_1
        django_comments_1.user = auth_user_16
        django_comments_1.user_name = u'Dominique Guardiola'
        django_comments_1.user_email = u'contact@quinode.fr'
        django_comments_1.user_url = u'http://pfes.credis.org/profiles/admin/'
        django_comments_1.comment = u"Concernant l'affichage du nom de la structure plutot que le nom de l'utilisateur ou son pseudo, il est pr\xe9vu de distinguer quand il s'agit de quelqu'un qui a une fiche structure et qui parle au nom de sa structure. pareil pour le logo : si on parle au nom de la structure, c'est celui de la structure qui apparaitra.\nmais \xe7a n'empeche pas d'avoir un nom d'individu !!!"
        django_comments_1.submit_date = datetime.datetime(2010, 11, 2, 14, 43, 10, 719875)
        django_comments_1.ip_address = '62.147.185.212'
        django_comments_1.is_public = True
        django_comments_1.is_removed = False
        django_comments_1.save()

        django_comments_2 = Comment()
        django_comments_2.content_type = ContentType.objects.get(app_label="chantiers", model="chantier")
        django_comments_2.object_pk = u'5'
        django_comments_2.site = django_site_1
        django_comments_2.user = auth_user_16
        django_comments_2.user_name = u'Dominique Guardiola'
        django_comments_2.user_email = u'contact@quinode.fr'
        django_comments_2.user_url = u'http://pfes.credis.org/profiles/admin/'
        django_comments_2.comment = u'Je viens d\'ajouter dans les documents de travail \xe0 droite le sch\xe9ma "Description de l\'application" de base. \nC\'est les fonctions de la plate-forme, qui sera \xe9galement mise \xe0 dispositions des r\xe9seaux qui voudront l\'utiliser pour synchroniser leurs donn\xe9es.  \nVoir aussi sur le blog : \nhttp://blog.credis.org/post/2010/11/02/Schema-de-l-application-de-base'
        django_comments_2.submit_date = datetime.datetime(2010, 11, 2, 17, 14, 34, 325033)
        django_comments_2.ip_address = '62.147.185.212'
        django_comments_2.is_public = True
        django_comments_2.is_removed = False
        django_comments_2.save()

        django_comments_3 = Comment()
        django_comments_3.content_type = ContentType.objects.get(app_label="chantiers", model="chantier")
        django_comments_3.object_pk = u'5'
        django_comments_3.site = django_site_1
        django_comments_3.user = auth_user_2
        django_comments_3.user_name = u'Marc DIGONNET'
        django_comments_3.user_email = u'mdigonnet@orange.fr'
        django_comments_3.user_url = u'http://pfes.credis.org/profiles/mdigonnet/'
        django_comments_3.comment = u'Impressionnant\xa0!!!\nJe vais me familiariser et apporter, si possible, quelques commentaires.\nMarc.'
        django_comments_3.submit_date = datetime.datetime(2010, 11, 2, 23, 28, 12, 284719)
        django_comments_3.ip_address = '86.193.61.168'
        django_comments_3.is_public = True
        django_comments_3.is_removed = False
        django_comments_3.save()

        django_comments_4 = Comment()
        django_comments_4.content_type = ContentType.objects.get(app_label="crowdsourcing", model="survey")
        django_comments_4.object_pk = u'1'
        django_comments_4.site = django_site_1
        django_comments_4.user = auth_user_16
        django_comments_4.user_name = u'Dominique Guardiola'
        django_comments_4.user_email = u'contact@quinode.fr'
        django_comments_4.user_url = u'http://pfes.credis.org/profiles/admin/'
        django_comments_4.comment = u"Pascal, sur la confidentialit\xe9 des \xe9changes, je suppose que Emmanuelle parlait de ce qu'on fait ici, maintenant : \xe0 savoir que ces discussions sur la mise en place de l'outil ne seront pas forc\xe9ment publi\xe9es (ce qui veut dire : l\xe2chez-vous!)"
        django_comments_4.submit_date = datetime.datetime(2010, 11, 4, 21, 51, 46, 834814)
        django_comments_4.ip_address = '81.56.151.113'
        django_comments_4.is_public = True
        django_comments_4.is_removed = False
        django_comments_4.save()

        django_comments_5 = Comment()
        django_comments_5.content_type = ContentType.objects.get(app_label="crowdsourcing", model="survey")
        django_comments_5.object_pk = u'2'
        django_comments_5.site = django_site_1
        django_comments_5.user = auth_user_16
        django_comments_5.user_name = u'Dominique Guardiola'
        django_comments_5.user_email = u'contact@quinode.fr'
        django_comments_5.user_url = u'http://pfes.credis.org/profiles/admin/'
        django_comments_5.comment = u"Sur la messagerie interne, je vois d\xe9j\xe0 une situation ou c'est n\xe9cessaire : l'archivage sur le site de certains messages relatifs \xe0 la gestion de la fiche structure. Exemple : une fiche structure est reli\xe9e \xe0 deux contacts, le responsable l\xe9gal, qui a un compte sur le site, et une employ\xe9e-animatrice.\nSi on veut garder une trace des \xe9changes qui ont pu avoir lieu entre l'employ\xe9e et des visiteurs via le site, la boite locale peut \xeatre utile. Ce qui n'emp\xeache pas de syst\xe9matiquement tout renvoyer en copie vers la boite email de la personne."
        django_comments_5.submit_date = datetime.datetime(2010, 11, 5, 13, 50, 55, 63394)
        django_comments_5.ip_address = '62.147.185.212'
        django_comments_5.is_public = True
        django_comments_5.is_removed = False
        django_comments_5.save()

        from django.contrib.comments.models import CommentFlag



        from invitation.models import InvitationKey

        invitation_invitationkey_1 = InvitationKey()
        invitation_invitationkey_1.key = u'ab9c6f7ee8fe72c59a3217c4b381231360cb69d4'
        invitation_invitationkey_1.date_invited = datetime.datetime(2010, 10, 18, 22, 15, 54, 665839)
        invitation_invitationkey_1.from_user = auth_user_8
        invitation_invitationkey_1.save()

        invitation_invitationkey_2 = InvitationKey()
        invitation_invitationkey_2.key = u'e69444b940a7c514309a4b7b7acf1b0129143d9c'
        invitation_invitationkey_2.date_invited = datetime.datetime(2010, 11, 4, 21, 30, 46, 600549)
        invitation_invitationkey_2.from_user = auth_user_15
        invitation_invitationkey_2.save()

        from organisme.models import Organisme


        from crowdsourcing.models import SurveyReportDisplay


        from taggit.models import Tag

        taggit_tag_1 = Tag()
        taggit_tag_1.name = u'charte'
        taggit_tag_1.slug = u'charte'
        taggit_tag_1.save()

        from taggit.models import TaggedItem

        taggit_taggeditem_1 = TaggedItem()
        taggit_taggeditem_1.tag = taggit_tag_1
        taggit_taggeditem_1.object_id = 1
        taggit_taggeditem_1.content_type = ContentType.objects.get(app_label="chantiers", model="chantier")
        taggit_taggeditem_1.save()

        from chantiers.models import Chantier

        chantiers_chantier_1 = Chantier()
        chantiers_chantier_1.nom = u'Auto-\xe9valuation'
        chantiers_chantier_1.slug = u'auto-evaluation'
        chantiers_chantier_1.description = u"Construire ensemble un outil d'auto-\xe9valuation de nos progr\xe8s en mati\xe8re de d\xe9veloppement durable et solidaire afin de mettre en place une d\xe9marche collective de progr\xe8s pour l'ensemble des participants de la plate-forme.\r\nVous pouvez en permanence commenter le sujet ou le documenter en postant de nouveaux documents ressource."
        chantiers_chantier_1.gdocs_folder = u'Evaluation'
        chantiers_chantier_1.gdocs_email = u'web@credis.org'
        chantiers_chantier_1.gdocs_pass = u'arz449i8'
        chantiers_chantier_1.date_creation = datetime.datetime(2010, 10, 13, 16, 29, 48)
        chantiers_chantier_1.date_modification = datetime.datetime(2010, 10, 15, 17, 45, 13, 716423)
        chantiers_chantier_1.position = 1
        chantiers_chantier_1.save()

        chantiers_chantier_2 = Chantier()
        chantiers_chantier_2.nom = u'Les th\xe9matiques'
        chantiers_chantier_2.slug = u'les-thematiques'
        chantiers_chantier_2.description = u'Proposer et documenter des th\xe9matiques qui pourront mobiliser les b\xe2tisseurs.\r\nVous pouvez en permanence commenter le sujet ou le documenter en postant de nouveaux documents ressource.'
        chantiers_chantier_2.gdocs_folder = u''
        chantiers_chantier_2.gdocs_email = u''
        chantiers_chantier_2.gdocs_pass = u''
        chantiers_chantier_2.date_creation = datetime.datetime(2010, 10, 14, 16, 51, 23)
        chantiers_chantier_2.date_modification = datetime.datetime(2010, 10, 15, 17, 51, 15, 293216)
        chantiers_chantier_2.position = 3
        chantiers_chantier_2.save()

        chantiers_chantier_3 = Chantier()
        chantiers_chantier_3.nom = u'Ressources de chacun'
        chantiers_chantier_3.slug = u'nos-ressources'
        chantiers_chantier_3.description = u"Collecter et partager d'ores et d\xe9j\xe0 des ressources de membres du collectif pour la plate-forme.\r\nVous pouvez en permanence commenter le sujet ou le documenter en postant de nouveaux documents ressource."
        chantiers_chantier_3.gdocs_folder = u''
        chantiers_chantier_3.gdocs_email = u''
        chantiers_chantier_3.gdocs_pass = u''
        chantiers_chantier_3.date_creation = datetime.datetime(2010, 10, 13, 16, 29, 58)
        chantiers_chantier_3.date_modification = datetime.datetime(2010, 10, 15, 17, 55, 1, 794799)
        chantiers_chantier_3.position = 2
        chantiers_chantier_3.save()

        chantiers_chantier_4 = Chantier()
        chantiers_chantier_4.nom = u'La Charte'
        chantiers_chantier_4.slug = u'la-charte'
        chantiers_chantier_4.description = u"Discuter ensemble d'une charte des acteurs de la plate-forme en comparant les travaux d'une vingtaine de r\xe9seaux associatifs ou coop\xe9ratifs \xe0 travers la France.\r\nVous pouvez en permanence commenter le sujet ou le documenter en postant de nouveaux documents ressource."
        chantiers_chantier_4.gdocs_folder = u'Chartes'
        chantiers_chantier_4.gdocs_email = u'web@credis.org'
        chantiers_chantier_4.gdocs_pass = u'arz449i8'
        chantiers_chantier_4.date_creation = datetime.datetime(2010, 10, 11, 12, 51, 9)
        chantiers_chantier_4.date_modification = datetime.datetime(2010, 10, 26, 17, 54, 37, 349790)
        chantiers_chantier_4.position = 0
        chantiers_chantier_4.save()

        chantiers_chantier_5 = Chantier()
        chantiers_chantier_5.nom = u'Construction du site'
        chantiers_chantier_5.slug = u'construction-du-site'
        chantiers_chantier_5.description = u'\xc9changer et r\xe9fl\xe9chir ensemble \xe0 des id\xe9es de fonctions, documents pr\xe9paratoires, sites web similaires...'
        chantiers_chantier_5.gdocs_folder = u'Construction'
        chantiers_chantier_5.gdocs_email = u'web@credis.org'
        chantiers_chantier_5.gdocs_pass = u'arz449i8'
        chantiers_chantier_5.date_creation = datetime.datetime(2010, 10, 14, 16, 52, 49)
        chantiers_chantier_5.date_modification = datetime.datetime(2010, 11, 1, 19, 46, 11, 676390)
        chantiers_chantier_5.position = 4
        chantiers_chantier_5.save()

        from local.models import OrganismeLocal


        from local.models import Relation


        from crowdsourcing.models import Survey

        crowdsourcing_survey_1 = Survey()
        crowdsourcing_survey_1.title = u'Profil utilisateur'
        crowdsourcing_survey_1.slug = u'profil-utilisateur'
        crowdsourcing_survey_1.tease = u'Un tout petit sondage tr\xe8s fonctionnel : quelques rep\xe8res pour la gestion des profils utilisateurs.\r\nNous parlons ici SEULEMENT des informations stock\xe9es pour les individus qui utiliseront le site, pas des fiches structures.\r\n'
        crowdsourcing_survey_1.description = u'Un tout petit sondage de test, tr\xe8s fonctionnel : quelques rep\xe8res pour la gestion des profils utilisateurs.\r\nNous parlons ici SEULEMENT des informations stock\xe9es pour les individus qui utiliseront le site, pas des fiches structures.\r\n'
        crowdsourcing_survey_1.thanks = u"Merci d'avoir r\xe9pondu !"
        crowdsourcing_survey_1.require_login = True
        crowdsourcing_survey_1.allow_multiple_submissions = False
        crowdsourcing_survey_1.moderate_submissions = False
        crowdsourcing_survey_1.allow_comments = False
        crowdsourcing_survey_1.allow_voting = False
        crowdsourcing_survey_1.archive_policy = 1
        crowdsourcing_survey_1.starts_at = datetime.datetime(2010, 11, 1, 19, 19, 34)
        crowdsourcing_survey_1.survey_date = datetime.date(2010, 11, 1)
        crowdsourcing_survey_1.ends_at = None
        crowdsourcing_survey_1.is_published = True
        crowdsourcing_survey_1.email = u'dguardiola@credis.org'
        crowdsourcing_survey_1.site = django_site_1
        crowdsourcing_survey_1.flickr_group_id = u''
        crowdsourcing_survey_1.flickr_group_name = u''
        crowdsourcing_survey_1.default_report = None
        crowdsourcing_survey_1.save()

        crowdsourcing_survey_2 = Survey()
        crowdsourcing_survey_2.title = u'Points de la Charte'
        crowdsourcing_survey_2.slug = u'points-de-la-charte'
        crowdsourcing_survey_2.tease = u"Nous vous proposons une synth\xe8se des points-cl\xe9s \xe9voqu\xe9s jusqu'\xe0 pr\xe9sent.\r\nVous pouvez indiquer pour chaque point si vous \xeates favorable ou d\xe9favorable ou si vous estimez que ce point a besoin d'\xeatre discut\xe9. Vous pouvez dans tous les cas commenter ou proposer une re-formulation de ce point dans la case pr\xe9vue \xe0 cet effet sous chaque question.\r\n\r\nCette plate-forme web collaborative d'\xe9changes solidaires a pour objet..."
        crowdsourcing_survey_2.description = u"Nous vous proposons une synth\xe8se des points-cl\xe9s \xe9voqu\xe9s jusqu'\xe0 pr\xe9sent.\r\nVous pouvez indiquer pour chaque point si vous \xeates favorable ou d\xe9favorable ou si vous estimez que ce point a besoin d'\xeatre discut\xe9. Vous pouvez dans tous les cas commenter ou proposer une re-formulation de ce point dans la case pr\xe9vue \xe0 cet effet sous chaque question.\r\n\r\nCette plate-forme web collaborative d'\xe9changes solidaires a pour objet..."
        crowdsourcing_survey_2.thanks = u"Merci d'avoir r\xe9pondu \xe0 ce sondage !"
        crowdsourcing_survey_2.require_login = True
        crowdsourcing_survey_2.allow_multiple_submissions = False
        crowdsourcing_survey_2.moderate_submissions = False
        crowdsourcing_survey_2.allow_comments = False
        crowdsourcing_survey_2.allow_voting = False
        crowdsourcing_survey_2.archive_policy = 1
        crowdsourcing_survey_2.starts_at = datetime.datetime(2010, 10, 26, 17, 29, 47)
        crowdsourcing_survey_2.survey_date = datetime.date(2010, 10, 26)
        crowdsourcing_survey_2.ends_at = None
        crowdsourcing_survey_2.is_published = True
        crowdsourcing_survey_2.email = u''
        crowdsourcing_survey_2.site = django_site_1
        crowdsourcing_survey_2.flickr_group_id = u''
        crowdsourcing_survey_2.flickr_group_name = u''
        crowdsourcing_survey_2.default_report = None
        crowdsourcing_survey_2.save()

        from crowdsourcing.models import Question

        crowdsourcing_question_1 = Question()
        crowdsourcing_question_1.survey = crowdsourcing_survey_1
        crowdsourcing_question_1.fieldname = u'Inscription'
        crowdsourcing_question_1.question = u"Comment avez-vous trouv\xe9 la proc\xe9dure d'inscription sur ce site ?"
        crowdsourcing_question_1.label = u'Proc\xe9dure inscription'
        crowdsourcing_question_1.help_text = u''
        crowdsourcing_question_1.required = True
        crowdsourcing_question_1.order = 0
        crowdsourcing_question_1.option_type = u'choice'
        crowdsourcing_question_1.numeric_is_int = True
        crowdsourcing_question_1.options = u'Standard, pas de souci particulier\r\nTrop long\r\nTrop compliqu\xe9 (expliquez)'
        crowdsourcing_question_1.map_icons = u''
        crowdsourcing_question_1.answer_is_public = True
        crowdsourcing_question_1.use_as_filter = False
        crowdsourcing_question_1.save()

        crowdsourcing_question_2 = Question()
        crowdsourcing_question_2.survey = crowdsourcing_survey_2
        crowdsourcing_question_2.fieldname = u'Developpement'
        crowdsourcing_question_2.question = u"...de stimuler le d\xe9veloppement d'activit\xe9s \xe9conomiques d'initiatives locales, mon\xe9taires ou non, favorisant la coop\xe9ration, le partenariat et l'action citoyenne."
        crowdsourcing_question_2.label = u'D\xe9veloppement \xe9conomique'
        crowdsourcing_question_2.help_text = u''
        crowdsourcing_question_2.required = True
        crowdsourcing_question_2.order = 0
        crowdsourcing_question_2.option_type = u'choice'
        crowdsourcing_question_2.numeric_is_int = True
        crowdsourcing_question_2.options = u'favorable\r\nd\xe9favorable\r\n\xe0 discuter'
        crowdsourcing_question_2.map_icons = u''
        crowdsourcing_question_2.answer_is_public = True
        crowdsourcing_question_2.use_as_filter = False
        crowdsourcing_question_2.save()

        crowdsourcing_question_3 = Question()
        crowdsourcing_question_3.survey = crowdsourcing_survey_2
        crowdsourcing_question_3.fieldname = u'Environnement'
        crowdsourcing_question_3.question = u"Ce d\xe9veloppement doit \xeatre au service d'une meilleure qualit\xe9 de vie pour tous et de la pr\xe9servation des ressources naturelles en activant des solidarit\xe9s entre individus d'un territoire, entre territoires et entre activit\xe9s."
        crowdsourcing_question_3.label = u'Environnement / Qualit\xe9 de vie'
        crowdsourcing_question_3.help_text = u''
        crowdsourcing_question_3.required = True
        crowdsourcing_question_3.order = 1
        crowdsourcing_question_3.option_type = u'choice'
        crowdsourcing_question_3.numeric_is_int = True
        crowdsourcing_question_3.options = u'favorable\r\nd\xe9favorable\r\n\xe0 discuter'
        crowdsourcing_question_3.map_icons = u''
        crowdsourcing_question_3.answer_is_public = True
        crowdsourcing_question_3.use_as_filter = False
        crowdsourcing_question_3.save()

        crowdsourcing_question_4 = Question()
        crowdsourcing_question_4.survey = crowdsourcing_survey_1
        crowdsourcing_question_4.fieldname = u'Adresse'
        crowdsourcing_question_4.question = u"Etant donn\xe9 le champs d'action r\xe9gional du site, trouvez-vous normal que nous demandions l'adresse ou au moins le code postal de l'utilisateur ?\r\nLe but est de pouvoir proposer en page d'accueil des contenus localis\xe9s pr\xe8s de chez lui."
        crowdsourcing_question_4.label = u"Demander l'adresse"
        crowdsourcing_question_4.help_text = u''
        crowdsourcing_question_4.required = True
        crowdsourcing_question_4.order = 1
        crowdsourcing_question_4.option_type = u'choice'
        crowdsourcing_question_4.numeric_is_int = True
        crowdsourcing_question_4.options = u"Oui, c'est normal\r\n\xc7a doit rester une option\r\n\xc7a ne sert \xe0 rien"
        crowdsourcing_question_4.map_icons = u''
        crowdsourcing_question_4.answer_is_public = True
        crowdsourcing_question_4.use_as_filter = False
        crowdsourcing_question_4.save()

        crowdsourcing_question_5 = Question()
        crowdsourcing_question_5.survey = crowdsourcing_survey_2
        crowdsourcing_question_5.fieldname = u'Progres'
        crowdsourcing_question_5.question = u'Acceptant le principe de d\xe9marche de progr\xe8s, les structures inscrites sur la plate-forme ...\r\n(c\'est le terme "d\xe9marche de progr\xe8s" qui est propos\xe9 ici)'
        crowdsourcing_question_5.label = u'D\xe9marche de progr\xe8s'
        crowdsourcing_question_5.help_text = u''
        crowdsourcing_question_5.required = True
        crowdsourcing_question_5.order = 2
        crowdsourcing_question_5.option_type = u'choice'
        crowdsourcing_question_5.numeric_is_int = True
        crowdsourcing_question_5.options = u'favorable\r\nd\xe9favorable\r\n\xe0 discuter'
        crowdsourcing_question_5.map_icons = u''
        crowdsourcing_question_5.answer_is_public = True
        crowdsourcing_question_5.use_as_filter = False
        crowdsourcing_question_5.save()

        crowdsourcing_question_6 = Question()
        crowdsourcing_question_6.survey = crowdsourcing_survey_1
        crowdsourcing_question_6.fieldname = u'Geolocalisation'
        crowdsourcing_question_6.question = u'En ce qui concerne les utilisateurs nouveaux, qui ne sont pas enregistr\xe9s, il est possible de les localiser gr\xe2ce \xe0 leur adresse publique internet (la fameuse "adresse IP").\r\nPensez-vous qu\'il soit int\xe9ressant de proposer directement du contenu g\xe9o-localis\xe9 (en clair : une carte centr\xe9e sur la localisation du visiteur plut\xf4t que sur un centre arbitraire), gr\xe2ce \xe0 cette information.'
        crowdsourcing_question_6.label = u'G\xe9o-localisation des anonymes'
        crowdsourcing_question_6.help_text = u''
        crowdsourcing_question_6.required = True
        crowdsourcing_question_6.order = 2
        crowdsourcing_question_6.option_type = u'choice'
        crowdsourcing_question_6.numeric_is_int = True
        crowdsourcing_question_6.options = u"Oui, si l'information est disponible, autant l'utiliser\r\nNon, c'est une atteinte \xe0 la vie priv\xe9e (ou peut \xeatre v\xe9cu comme tel)\r\nProposer la possibilit\xe9 d'\xeatre localis\xe9 sans s'inscrire"
        crowdsourcing_question_6.map_icons = u''
        crowdsourcing_question_6.answer_is_public = True
        crowdsourcing_question_6.use_as_filter = False
        crowdsourcing_question_6.save()

        crowdsourcing_question_7 = Question()
        crowdsourcing_question_7.survey = crowdsourcing_survey_2
        crowdsourcing_question_7.fieldname = u'AutoEvaluation'
        crowdsourcing_question_7.question = u"...s'engagent \xe0 \xe9valuer leurs pratiques sociales, \xe9conomiques, environnementales et de gouvernance dans un esprit de transparence et acceptent le principe de droit de regard des membres de la plate-forme."
        crowdsourcing_question_7.label = u'Auto-Evaluation'
        crowdsourcing_question_7.help_text = u''
        crowdsourcing_question_7.required = True
        crowdsourcing_question_7.order = 3
        crowdsourcing_question_7.option_type = u'choice'
        crowdsourcing_question_7.numeric_is_int = True
        crowdsourcing_question_7.options = u'favorable\r\nd\xe9favorable\r\n\xe0 discuter'
        crowdsourcing_question_7.map_icons = u''
        crowdsourcing_question_7.answer_is_public = True
        crowdsourcing_question_7.use_as_filter = False
        crowdsourcing_question_7.save()

        crowdsourcing_question_8 = Question()
        crowdsourcing_question_8.survey = crowdsourcing_survey_1
        crowdsourcing_question_8.fieldname = u'NomUtilisateur'
        crowdsourcing_question_8.question = u"Vous avez sur le site un nom d'utilisateur, qui est libre, c'est un pseudo diff\xe9rent de votre nom et diff\xe9rent de votre courriel. Il pourra \xeatre modifi\xe9 \xe0 loisir.\r\nLes adresse courriel ne sont jamais affich\xe9s en clair.\r\nPour identifier les membres, dans leurs commentaires par exemple, nous proposons que seuls les utilisateurs inscrits puissent voir les vrais noms des autres membres, et que les anonymes (tout comme les moteurs de recherche) ne puissent afficher que le nom d'utilisateur."
        crowdsourcing_question_8.label = u"Nom d'utilisateur"
        crowdsourcing_question_8.help_text = u''
        crowdsourcing_question_8.required = True
        crowdsourcing_question_8.order = 3
        crowdsourcing_question_8.option_type = u'choice'
        crowdsourcing_question_8.numeric_is_int = True
        crowdsourcing_question_8.options = u"Oui, c'est un bon compromis\r\nNon, il ne faut rien afficher du tout aux visiteurs anonymes\r\nJ'ai une autre proposition (d\xe9taillez)"
        crowdsourcing_question_8.map_icons = u''
        crowdsourcing_question_8.answer_is_public = True
        crowdsourcing_question_8.use_as_filter = False
        crowdsourcing_question_8.save()

        crowdsourcing_question_9 = Question()
        crowdsourcing_question_9.survey = crowdsourcing_survey_1
        crowdsourcing_question_9.fieldname = u'Avatar'
        crowdsourcing_question_9.question = u'Beaucoup de sites sociaux utilisent un petite ic\xf4ne (un "avatar") pour identifier les utilisateurs.\r\nEst-ce que \xe7a vous parait :'
        crowdsourcing_question_9.label = u'Avatar'
        crowdsourcing_question_9.help_text = u''
        crowdsourcing_question_9.required = True
        crowdsourcing_question_9.order = 4
        crowdsourcing_question_9.option_type = u'choice'
        crowdsourcing_question_9.numeric_is_int = True
        crowdsourcing_question_9.options = u"Utile et sympathique, il en faut\r\nOK, mais il faudra proposer des ic\xf4nes, je ne veux pas mettre ma photo!\r\n\xc7a devrait \xeatre optionnel\r\nC'est compl\xe9tement inutile"
        crowdsourcing_question_9.map_icons = u''
        crowdsourcing_question_9.answer_is_public = True
        crowdsourcing_question_9.use_as_filter = False
        crowdsourcing_question_9.save()

        crowdsourcing_question_10 = Question()
        crowdsourcing_question_10.survey = crowdsourcing_survey_2
        crowdsourcing_question_10.fieldname = u'Individus'
        crowdsourcing_question_10.question = u"Ces structures deviennent alors de fait collaboratrices \xe0 part enti\xe8re de la plate-forme.\r\nPar ailleurs la plate-forme est ouverte \xe0 toute annonce d'\xe9changes solidaires \xe9manant de structure ou personne physique inscrites sur la plate-forme."
        crowdsourcing_question_10.label = u'Site ouvert \xe0 tous'
        crowdsourcing_question_10.help_text = u''
        crowdsourcing_question_10.required = True
        crowdsourcing_question_10.order = 4
        crowdsourcing_question_10.option_type = u'choice'
        crowdsourcing_question_10.numeric_is_int = True
        crowdsourcing_question_10.options = u'favorable\r\nd\xe9favorable\r\n\xe0 discuter'
        crowdsourcing_question_10.map_icons = u''
        crowdsourcing_question_10.answer_is_public = True
        crowdsourcing_question_10.use_as_filter = False
        crowdsourcing_question_10.save()

        crowdsourcing_question_11 = Question()
        crowdsourcing_question_11.survey = crowdsourcing_survey_1
        crowdsourcing_question_11.fieldname = u'Messagerie'
        crowdsourcing_question_11.question = u"Compte tenu de nos objectifs pour cette plate-forme ( agendas partag\xe9s, annonces, actualit\xe9s ) , que pensez-vous de d'une messagerie interne au site, c'est \xe0 dire uniquement consultable sur le site ?"
        crowdsourcing_question_11.label = u'Messagerie interne'
        crowdsourcing_question_11.help_text = u''
        crowdsourcing_question_11.required = True
        crowdsourcing_question_11.order = 5
        crowdsourcing_question_11.option_type = u'choice'
        crowdsourcing_question_11.numeric_is_int = True
        crowdsourcing_question_11.options = u"\xc7a peut \xeatre utile\r\nOui, mais il faut que \xe7a m'envoie les messages sur mon email aussi\r\n\xc7a fait double emploi avec le courriel en g\xe9n\xe9ral, inutile\r\n"
        crowdsourcing_question_11.map_icons = u''
        crowdsourcing_question_11.answer_is_public = True
        crowdsourcing_question_11.use_as_filter = False
        crowdsourcing_question_11.save()

        crowdsourcing_question_12 = Question()
        crowdsourcing_question_12.survey = crowdsourcing_survey_2
        crowdsourcing_question_12.fieldname = u'Criteres'
        crowdsourcing_question_12.question = u"Les crit\xe8res pour l'inscription des structures comme pour les \xe9changes solidaires sont rassembl\xe9s dans un outil d'auto-\xe9valuation bas\xe9 sur les piliers du d\xe9veloppement durable pr\xe9sent\xe9 en annexe."
        crowdsourcing_question_12.label = u"Crit\xe8res d'auto-\xe9valuation"
        crowdsourcing_question_12.help_text = u''
        crowdsourcing_question_12.required = True
        crowdsourcing_question_12.order = 5
        crowdsourcing_question_12.option_type = u'choice'
        crowdsourcing_question_12.numeric_is_int = True
        crowdsourcing_question_12.options = u'favorable\r\nd\xe9favorable\r\n\xe0 discuter'
        crowdsourcing_question_12.map_icons = u''
        crowdsourcing_question_12.answer_is_public = True
        crowdsourcing_question_12.use_as_filter = False
        crowdsourcing_question_12.save()

        crowdsourcing_question_13 = Question()
        crowdsourcing_question_13.survey = crowdsourcing_survey_1
        crowdsourcing_question_13.fieldname = u'Services'
        crowdsourcing_question_13.question = u"Utilisez-vous assez r\xe9guli\xe8rement l'un des services web suivants :"
        crowdsourcing_question_13.label = u'Services web'
        crowdsourcing_question_13.help_text = u''
        crowdsourcing_question_13.required = True
        crowdsourcing_question_13.order = 6
        crowdsourcing_question_13.option_type = u'bool_list'
        crowdsourcing_question_13.numeric_is_int = True
        crowdsourcing_question_13.options = u'facebook\r\ntwitter\r\ngoogle Agenda\r\ngoogle Documents\r\nGMail\r\nViadeo\r\nLinkedIn\r\n'
        crowdsourcing_question_13.map_icons = u''
        crowdsourcing_question_13.answer_is_public = True
        crowdsourcing_question_13.use_as_filter = False
        crowdsourcing_question_13.save()

        crowdsourcing_question_14 = Question()
        crowdsourcing_question_14.survey = crowdsourcing_survey_2
        crowdsourcing_question_14.fieldname = u'Collectif'
        crowdsourcing_question_14.question = u"Le collectif mobilis\xe9 sur la base de l'ensemble des parties prenantes du projet proc\xe8de \xe0 l'ensemble des choix de construction et de gestion de la plate-forme dans un esprit constructif de force de proposition et de partage et dans le respect de la confidentialit\xe9 des \xe9changes. "
        crowdsourcing_question_14.label = u'Construction collective'
        crowdsourcing_question_14.help_text = u''
        crowdsourcing_question_14.required = True
        crowdsourcing_question_14.order = 6
        crowdsourcing_question_14.option_type = u'choice'
        crowdsourcing_question_14.numeric_is_int = True
        crowdsourcing_question_14.options = u'favorable\r\nd\xe9favorable\r\n\xe0 discuter'
        crowdsourcing_question_14.map_icons = u''
        crowdsourcing_question_14.answer_is_public = True
        crowdsourcing_question_14.use_as_filter = False
        crowdsourcing_question_14.save()

        crowdsourcing_question_15 = Question()
        crowdsourcing_question_15.survey = crowdsourcing_survey_2
        crowdsourcing_question_15.fieldname = u'Gestion'
        crowdsourcing_question_15.question = u"Le CREDIS assume la gestion des conventions financi\xe8res pour une p\xe9riode de 36 mois \xe0 compter du 1er septembre 2010 en organisant des rencontres, en rendant compte aux collaborateurs de l'avanc\xe9e du projet, en \xe9ditant bilans et \xe9valuations."
        crowdsourcing_question_15.label = u'Gestion par le CREDIS'
        crowdsourcing_question_15.help_text = u''
        crowdsourcing_question_15.required = True
        crowdsourcing_question_15.order = 7
        crowdsourcing_question_15.option_type = u'choice'
        crowdsourcing_question_15.numeric_is_int = True
        crowdsourcing_question_15.options = u'favorable\r\nd\xe9favorable\r\n\xe0 discuter'
        crowdsourcing_question_15.map_icons = u''
        crowdsourcing_question_15.answer_is_public = True
        crowdsourcing_question_15.use_as_filter = False
        crowdsourcing_question_15.save()

        from crowdsourcing.models import Submission

        crowdsourcing_submission_1 = Submission()
        crowdsourcing_submission_1.survey = crowdsourcing_survey_1
        crowdsourcing_submission_1.user = auth_user_1
        crowdsourcing_submission_1.ip_address = '62.147.209.208'
        crowdsourcing_submission_1.submitted_at = datetime.datetime(2010, 11, 4, 11, 33, 0, 966303)
        crowdsourcing_submission_1.session_key = u''
        crowdsourcing_submission_1.featured = False
        crowdsourcing_submission_1.is_public = True
        crowdsourcing_submission_1.save()

        crowdsourcing_submission_2 = Submission()
        crowdsourcing_submission_2.survey = crowdsourcing_survey_2
        crowdsourcing_submission_2.user = auth_user_1
        crowdsourcing_submission_2.ip_address = '62.147.209.208'
        crowdsourcing_submission_2.submitted_at = datetime.datetime(2010, 11, 4, 11, 2, 3, 547777)
        crowdsourcing_submission_2.session_key = u''
        crowdsourcing_submission_2.featured = False
        crowdsourcing_submission_2.is_public = True
        crowdsourcing_submission_2.save()

        crowdsourcing_submission_3 = Submission()
        crowdsourcing_submission_3.survey = crowdsourcing_survey_1
        crowdsourcing_submission_3.user = auth_user_4
        crowdsourcing_submission_3.ip_address = '90.42.157.25'
        crowdsourcing_submission_3.submitted_at = datetime.datetime(2010, 11, 2, 12, 12, 42, 51211)
        crowdsourcing_submission_3.session_key = u''
        crowdsourcing_submission_3.featured = False
        crowdsourcing_submission_3.is_public = True
        crowdsourcing_submission_3.save()

        crowdsourcing_submission_4 = Submission()
        crowdsourcing_submission_4.survey = crowdsourcing_survey_2
        crowdsourcing_submission_4.user = auth_user_4
        crowdsourcing_submission_4.ip_address = '90.42.157.25'
        crowdsourcing_submission_4.submitted_at = datetime.datetime(2010, 11, 2, 11, 51, 36, 560252)
        crowdsourcing_submission_4.session_key = u''
        crowdsourcing_submission_4.featured = False
        crowdsourcing_submission_4.is_public = True
        crowdsourcing_submission_4.save()

        crowdsourcing_submission_5 = Submission()
        crowdsourcing_submission_5.survey = crowdsourcing_survey_2
        crowdsourcing_submission_5.user = auth_user_6
        crowdsourcing_submission_5.ip_address = '86.211.47.126'
        crowdsourcing_submission_5.submitted_at = datetime.datetime(2010, 11, 2, 10, 54, 31, 748915)
        crowdsourcing_submission_5.session_key = u''
        crowdsourcing_submission_5.featured = False
        crowdsourcing_submission_5.is_public = True
        crowdsourcing_submission_5.save()

        crowdsourcing_submission_6 = Submission()
        crowdsourcing_submission_6.survey = crowdsourcing_survey_1
        crowdsourcing_submission_6.user = auth_user_16
        crowdsourcing_submission_6.ip_address = '62.147.185.212'
        crowdsourcing_submission_6.submitted_at = datetime.datetime(2010, 11, 1, 20, 21, 55, 21590)
        crowdsourcing_submission_6.session_key = u''
        crowdsourcing_submission_6.featured = False
        crowdsourcing_submission_6.is_public = True
        crowdsourcing_submission_6.save()

        crowdsourcing_submission_7 = Submission()
        crowdsourcing_submission_7.survey = crowdsourcing_survey_2
        crowdsourcing_submission_7.user = auth_user_16
        crowdsourcing_submission_7.ip_address = '81.56.151.113'
        crowdsourcing_submission_7.submitted_at = datetime.datetime(2010, 10, 26, 23, 40, 42, 381394)
        crowdsourcing_submission_7.session_key = u''
        crowdsourcing_submission_7.featured = False
        crowdsourcing_submission_7.is_public = True
        crowdsourcing_submission_7.save()

        from crowdsourcing.models import Answer

        crowdsourcing_answer_1 = Answer()
        crowdsourcing_answer_1.submission = crowdsourcing_submission_2
        crowdsourcing_answer_1.question = crowdsourcing_question_2
        crowdsourcing_answer_1.text_answer = u'favorable'
        crowdsourcing_answer_1.integer_answer = None
        crowdsourcing_answer_1.float_answer = None
        crowdsourcing_answer_1.boolean_answer = None
        crowdsourcing_answer_1.image_answer = u''
        crowdsourcing_answer_1.latitude = None
        crowdsourcing_answer_1.longitude = None
        crowdsourcing_answer_1.comment = u''
        crowdsourcing_answer_1.flickr_id = u''
        crowdsourcing_answer_1.photo_hash = None
        crowdsourcing_answer_1.save()

        crowdsourcing_answer_2 = Answer()
        crowdsourcing_answer_2.submission = crowdsourcing_submission_3
        crowdsourcing_answer_2.question = crowdsourcing_question_1
        crowdsourcing_answer_2.text_answer = u'Standard, pas de souci particulier'
        crowdsourcing_answer_2.integer_answer = None
        crowdsourcing_answer_2.float_answer = None
        crowdsourcing_answer_2.boolean_answer = None
        crowdsourcing_answer_2.image_answer = u''
        crowdsourcing_answer_2.latitude = None
        crowdsourcing_answer_2.longitude = None
        crowdsourcing_answer_2.comment = u''
        crowdsourcing_answer_2.flickr_id = u''
        crowdsourcing_answer_2.photo_hash = None
        crowdsourcing_answer_2.save()

        crowdsourcing_answer_3 = Answer()
        crowdsourcing_answer_3.submission = crowdsourcing_submission_7
        crowdsourcing_answer_3.question = crowdsourcing_question_2
        crowdsourcing_answer_3.text_answer = u'favorable'
        crowdsourcing_answer_3.integer_answer = None
        crowdsourcing_answer_3.float_answer = None
        crowdsourcing_answer_3.boolean_answer = None
        crowdsourcing_answer_3.image_answer = u''
        crowdsourcing_answer_3.latitude = None
        crowdsourcing_answer_3.longitude = None
        crowdsourcing_answer_3.comment = u''
        crowdsourcing_answer_3.flickr_id = u''
        crowdsourcing_answer_3.photo_hash = None
        crowdsourcing_answer_3.save()

        crowdsourcing_answer_4 = Answer()
        crowdsourcing_answer_4.submission = crowdsourcing_submission_5
        crowdsourcing_answer_4.question = crowdsourcing_question_2
        crowdsourcing_answer_4.text_answer = u'favorable'
        crowdsourcing_answer_4.integer_answer = None
        crowdsourcing_answer_4.float_answer = None
        crowdsourcing_answer_4.boolean_answer = None
        crowdsourcing_answer_4.image_answer = u''
        crowdsourcing_answer_4.latitude = None
        crowdsourcing_answer_4.longitude = None
        crowdsourcing_answer_4.comment = u''
        crowdsourcing_answer_4.flickr_id = u''
        crowdsourcing_answer_4.photo_hash = None
        crowdsourcing_answer_4.save()

        crowdsourcing_answer_5 = Answer()
        crowdsourcing_answer_5.submission = crowdsourcing_submission_4
        crowdsourcing_answer_5.question = crowdsourcing_question_2
        crowdsourcing_answer_5.text_answer = u'favorable'
        crowdsourcing_answer_5.integer_answer = None
        crowdsourcing_answer_5.float_answer = None
        crowdsourcing_answer_5.boolean_answer = None
        crowdsourcing_answer_5.image_answer = u''
        crowdsourcing_answer_5.latitude = None
        crowdsourcing_answer_5.longitude = None
        crowdsourcing_answer_5.comment = u''
        crowdsourcing_answer_5.flickr_id = u''
        crowdsourcing_answer_5.photo_hash = None
        crowdsourcing_answer_5.save()

        crowdsourcing_answer_6 = Answer()
        crowdsourcing_answer_6.submission = crowdsourcing_submission_6
        crowdsourcing_answer_6.question = crowdsourcing_question_1
        crowdsourcing_answer_6.text_answer = u'Standard, pas de souci particulier'
        crowdsourcing_answer_6.integer_answer = None
        crowdsourcing_answer_6.float_answer = None
        crowdsourcing_answer_6.boolean_answer = None
        crowdsourcing_answer_6.image_answer = u''
        crowdsourcing_answer_6.latitude = None
        crowdsourcing_answer_6.longitude = None
        crowdsourcing_answer_6.comment = u''
        crowdsourcing_answer_6.flickr_id = u''
        crowdsourcing_answer_6.photo_hash = None
        crowdsourcing_answer_6.save()

        crowdsourcing_answer_7 = Answer()
        crowdsourcing_answer_7.submission = crowdsourcing_submission_1
        crowdsourcing_answer_7.question = crowdsourcing_question_1
        crowdsourcing_answer_7.text_answer = u'Standard, pas de souci particulier'
        crowdsourcing_answer_7.integer_answer = None
        crowdsourcing_answer_7.float_answer = None
        crowdsourcing_answer_7.boolean_answer = None
        crowdsourcing_answer_7.image_answer = u''
        crowdsourcing_answer_7.latitude = None
        crowdsourcing_answer_7.longitude = None
        crowdsourcing_answer_7.comment = u"Un rappel par mail de l'identifiant et du mot de passe pour l'utilisateur dans des conditions de s\xe9curit\xe9 acceptable serait souhaitable"
        crowdsourcing_answer_7.flickr_id = u''
        crowdsourcing_answer_7.photo_hash = None
        crowdsourcing_answer_7.save()

        crowdsourcing_answer_8 = Answer()
        crowdsourcing_answer_8.submission = crowdsourcing_submission_1
        crowdsourcing_answer_8.question = crowdsourcing_question_4
        crowdsourcing_answer_8.text_answer = u"Oui, c'est normal"
        crowdsourcing_answer_8.integer_answer = None
        crowdsourcing_answer_8.float_answer = None
        crowdsourcing_answer_8.boolean_answer = None
        crowdsourcing_answer_8.image_answer = u''
        crowdsourcing_answer_8.latitude = None
        crowdsourcing_answer_8.longitude = None
        crowdsourcing_answer_8.comment = u"C'est normal que les autres membres de la plate forme connaissent la g\xe9olocalisation permanente. L'apparition publique de cette information devrait \xeatre maitris\xe9e par le membre\r\nCertaines pratiques sont nomades ou itin\xe9rantes, comment peut-on les prendre en compte ?\r\n"
        crowdsourcing_answer_8.flickr_id = u''
        crowdsourcing_answer_8.photo_hash = None
        crowdsourcing_answer_8.save()

        crowdsourcing_answer_9 = Answer()
        crowdsourcing_answer_9.submission = crowdsourcing_submission_3
        crowdsourcing_answer_9.question = crowdsourcing_question_4
        crowdsourcing_answer_9.text_answer = u'\xc7a doit rester une option'
        crowdsourcing_answer_9.integer_answer = None
        crowdsourcing_answer_9.float_answer = None
        crowdsourcing_answer_9.boolean_answer = None
        crowdsourcing_answer_9.image_answer = u''
        crowdsourcing_answer_9.latitude = None
        crowdsourcing_answer_9.longitude = None
        crowdsourcing_answer_9.comment = u"Une structure d'une r\xe9gion voisine pourrait apporter des r\xe9ponses \xe0 des besoins locaux non encore r\xe9solus sur le territoire "
        crowdsourcing_answer_9.flickr_id = u''
        crowdsourcing_answer_9.photo_hash = None
        crowdsourcing_answer_9.save()

        crowdsourcing_answer_10 = Answer()
        crowdsourcing_answer_10.submission = crowdsourcing_submission_2
        crowdsourcing_answer_10.question = crowdsourcing_question_3
        crowdsourcing_answer_10.text_answer = u'\xe0 discuter'
        crowdsourcing_answer_10.integer_answer = None
        crowdsourcing_answer_10.float_answer = None
        crowdsourcing_answer_10.boolean_answer = None
        crowdsourcing_answer_10.image_answer = u''
        crowdsourcing_answer_10.latitude = None
        crowdsourcing_answer_10.longitude = None
        crowdsourcing_answer_10.comment = u'Il est difficile de r\xe9duire l\'ensemble du spectre des chartes \xe9cologiques existantes sur la simple "pr\xe9servation des ressources naturelles". Cet aspect m\xe9rite d\'\xeatre largement approfondi.'
        crowdsourcing_answer_10.flickr_id = u''
        crowdsourcing_answer_10.photo_hash = None
        crowdsourcing_answer_10.save()

        crowdsourcing_answer_11 = Answer()
        crowdsourcing_answer_11.submission = crowdsourcing_submission_6
        crowdsourcing_answer_11.question = crowdsourcing_question_4
        crowdsourcing_answer_11.text_answer = u"Oui, c'est normal"
        crowdsourcing_answer_11.integer_answer = None
        crowdsourcing_answer_11.float_answer = None
        crowdsourcing_answer_11.boolean_answer = None
        crowdsourcing_answer_11.image_answer = u''
        crowdsourcing_answer_11.latitude = None
        crowdsourcing_answer_11.longitude = None
        crowdsourcing_answer_11.comment = u''
        crowdsourcing_answer_11.flickr_id = u''
        crowdsourcing_answer_11.photo_hash = None
        crowdsourcing_answer_11.save()

        crowdsourcing_answer_12 = Answer()
        crowdsourcing_answer_12.submission = crowdsourcing_submission_4
        crowdsourcing_answer_12.question = crowdsourcing_question_3
        crowdsourcing_answer_12.text_answer = u'favorable'
        crowdsourcing_answer_12.integer_answer = None
        crowdsourcing_answer_12.float_answer = None
        crowdsourcing_answer_12.boolean_answer = None
        crowdsourcing_answer_12.image_answer = u''
        crowdsourcing_answer_12.latitude = None
        crowdsourcing_answer_12.longitude = None
        crowdsourcing_answer_12.comment = u''
        crowdsourcing_answer_12.flickr_id = u''
        crowdsourcing_answer_12.photo_hash = None
        crowdsourcing_answer_12.save()

        crowdsourcing_answer_13 = Answer()
        crowdsourcing_answer_13.submission = crowdsourcing_submission_5
        crowdsourcing_answer_13.question = crowdsourcing_question_3
        crowdsourcing_answer_13.text_answer = u'favorable'
        crowdsourcing_answer_13.integer_answer = None
        crowdsourcing_answer_13.float_answer = None
        crowdsourcing_answer_13.boolean_answer = None
        crowdsourcing_answer_13.image_answer = u''
        crowdsourcing_answer_13.latitude = None
        crowdsourcing_answer_13.longitude = None
        crowdsourcing_answer_13.comment = u''
        crowdsourcing_answer_13.flickr_id = u''
        crowdsourcing_answer_13.photo_hash = None
        crowdsourcing_answer_13.save()

        crowdsourcing_answer_14 = Answer()
        crowdsourcing_answer_14.submission = crowdsourcing_submission_7
        crowdsourcing_answer_14.question = crowdsourcing_question_3
        crowdsourcing_answer_14.text_answer = u'favorable'
        crowdsourcing_answer_14.integer_answer = None
        crowdsourcing_answer_14.float_answer = None
        crowdsourcing_answer_14.boolean_answer = None
        crowdsourcing_answer_14.image_answer = u''
        crowdsourcing_answer_14.latitude = None
        crowdsourcing_answer_14.longitude = None
        crowdsourcing_answer_14.comment = u''
        crowdsourcing_answer_14.flickr_id = u''
        crowdsourcing_answer_14.photo_hash = None
        crowdsourcing_answer_14.save()

        crowdsourcing_answer_15 = Answer()
        crowdsourcing_answer_15.submission = crowdsourcing_submission_5
        crowdsourcing_answer_15.question = crowdsourcing_question_5
        crowdsourcing_answer_15.text_answer = u'favorable'
        crowdsourcing_answer_15.integer_answer = None
        crowdsourcing_answer_15.float_answer = None
        crowdsourcing_answer_15.boolean_answer = None
        crowdsourcing_answer_15.image_answer = u''
        crowdsourcing_answer_15.latitude = None
        crowdsourcing_answer_15.longitude = None
        crowdsourcing_answer_15.comment = u''
        crowdsourcing_answer_15.flickr_id = u''
        crowdsourcing_answer_15.photo_hash = None
        crowdsourcing_answer_15.save()

        crowdsourcing_answer_16 = Answer()
        crowdsourcing_answer_16.submission = crowdsourcing_submission_4
        crowdsourcing_answer_16.question = crowdsourcing_question_5
        crowdsourcing_answer_16.text_answer = u'favorable'
        crowdsourcing_answer_16.integer_answer = None
        crowdsourcing_answer_16.float_answer = None
        crowdsourcing_answer_16.boolean_answer = None
        crowdsourcing_answer_16.image_answer = u''
        crowdsourcing_answer_16.latitude = None
        crowdsourcing_answer_16.longitude = None
        crowdsourcing_answer_16.comment = u''
        crowdsourcing_answer_16.flickr_id = u''
        crowdsourcing_answer_16.photo_hash = None
        crowdsourcing_answer_16.save()

        crowdsourcing_answer_17 = Answer()
        crowdsourcing_answer_17.submission = crowdsourcing_submission_1
        crowdsourcing_answer_17.question = crowdsourcing_question_6
        crowdsourcing_answer_17.text_answer = u"Non, c'est une atteinte \xe0 la vie priv\xe9e (ou peut \xeatre v\xe9cu comme tel)"
        crowdsourcing_answer_17.integer_answer = None
        crowdsourcing_answer_17.float_answer = None
        crowdsourcing_answer_17.boolean_answer = None
        crowdsourcing_answer_17.image_answer = u''
        crowdsourcing_answer_17.latitude = None
        crowdsourcing_answer_17.longitude = None
        crowdsourcing_answer_17.comment = u"Car il s'agit d'un traitement automatique non maitrisable par l'utilisateur."
        crowdsourcing_answer_17.flickr_id = u''
        crowdsourcing_answer_17.photo_hash = None
        crowdsourcing_answer_17.save()

        crowdsourcing_answer_18 = Answer()
        crowdsourcing_answer_18.submission = crowdsourcing_submission_2
        crowdsourcing_answer_18.question = crowdsourcing_question_5
        crowdsourcing_answer_18.text_answer = u'd\xe9favorable'
        crowdsourcing_answer_18.integer_answer = None
        crowdsourcing_answer_18.float_answer = None
        crowdsourcing_answer_18.boolean_answer = None
        crowdsourcing_answer_18.image_answer = u''
        crowdsourcing_answer_18.latitude = None
        crowdsourcing_answer_18.longitude = None
        crowdsourcing_answer_18.comment = u''
        crowdsourcing_answer_18.flickr_id = u''
        crowdsourcing_answer_18.photo_hash = None
        crowdsourcing_answer_18.save()

        crowdsourcing_answer_19 = Answer()
        crowdsourcing_answer_19.submission = crowdsourcing_submission_6
        crowdsourcing_answer_19.question = crowdsourcing_question_6
        crowdsourcing_answer_19.text_answer = u"Oui, si l'information est disponible, autant l'utiliser"
        crowdsourcing_answer_19.integer_answer = None
        crowdsourcing_answer_19.float_answer = None
        crowdsourcing_answer_19.boolean_answer = None
        crowdsourcing_answer_19.image_answer = u''
        crowdsourcing_answer_19.latitude = None
        crowdsourcing_answer_19.longitude = None
        crowdsourcing_answer_19.comment = u''
        crowdsourcing_answer_19.flickr_id = u''
        crowdsourcing_answer_19.photo_hash = None
        crowdsourcing_answer_19.save()

        crowdsourcing_answer_20 = Answer()
        crowdsourcing_answer_20.submission = crowdsourcing_submission_7
        crowdsourcing_answer_20.question = crowdsourcing_question_5
        crowdsourcing_answer_20.text_answer = u'favorable'
        crowdsourcing_answer_20.integer_answer = None
        crowdsourcing_answer_20.float_answer = None
        crowdsourcing_answer_20.boolean_answer = None
        crowdsourcing_answer_20.image_answer = u''
        crowdsourcing_answer_20.latitude = None
        crowdsourcing_answer_20.longitude = None
        crowdsourcing_answer_20.comment = u''
        crowdsourcing_answer_20.flickr_id = u''
        crowdsourcing_answer_20.photo_hash = None
        crowdsourcing_answer_20.save()

        crowdsourcing_answer_21 = Answer()
        crowdsourcing_answer_21.submission = crowdsourcing_submission_3
        crowdsourcing_answer_21.question = crowdsourcing_question_6
        crowdsourcing_answer_21.text_answer = u"Non, c'est une atteinte \xe0 la vie priv\xe9e (ou peut \xeatre v\xe9cu comme tel)"
        crowdsourcing_answer_21.integer_answer = None
        crowdsourcing_answer_21.float_answer = None
        crowdsourcing_answer_21.boolean_answer = None
        crowdsourcing_answer_21.image_answer = u''
        crowdsourcing_answer_21.latitude = None
        crowdsourcing_answer_21.longitude = None
        crowdsourcing_answer_21.comment = u'Big Brother ... il faudrait proposer cette possibilit\xe9 comme une option'
        crowdsourcing_answer_21.flickr_id = u''
        crowdsourcing_answer_21.photo_hash = None
        crowdsourcing_answer_21.save()

        crowdsourcing_answer_22 = Answer()
        crowdsourcing_answer_22.submission = crowdsourcing_submission_4
        crowdsourcing_answer_22.question = crowdsourcing_question_7
        crowdsourcing_answer_22.text_answer = u'favorable'
        crowdsourcing_answer_22.integer_answer = None
        crowdsourcing_answer_22.float_answer = None
        crowdsourcing_answer_22.boolean_answer = None
        crowdsourcing_answer_22.image_answer = u''
        crowdsourcing_answer_22.latitude = None
        crowdsourcing_answer_22.longitude = None
        crowdsourcing_answer_22.comment = u''
        crowdsourcing_answer_22.flickr_id = u''
        crowdsourcing_answer_22.photo_hash = None
        crowdsourcing_answer_22.save()

        crowdsourcing_answer_23 = Answer()
        crowdsourcing_answer_23.submission = crowdsourcing_submission_7
        crowdsourcing_answer_23.question = crowdsourcing_question_7
        crowdsourcing_answer_23.text_answer = u'favorable'
        crowdsourcing_answer_23.integer_answer = None
        crowdsourcing_answer_23.float_answer = None
        crowdsourcing_answer_23.boolean_answer = None
        crowdsourcing_answer_23.image_answer = u''
        crowdsourcing_answer_23.latitude = None
        crowdsourcing_answer_23.longitude = None
        crowdsourcing_answer_23.comment = u''
        crowdsourcing_answer_23.flickr_id = u''
        crowdsourcing_answer_23.photo_hash = None
        crowdsourcing_answer_23.save()

        crowdsourcing_answer_24 = Answer()
        crowdsourcing_answer_24.submission = crowdsourcing_submission_6
        crowdsourcing_answer_24.question = crowdsourcing_question_8
        crowdsourcing_answer_24.text_answer = u"Oui, c'est un bon compromis"
        crowdsourcing_answer_24.integer_answer = None
        crowdsourcing_answer_24.float_answer = None
        crowdsourcing_answer_24.boolean_answer = None
        crowdsourcing_answer_24.image_answer = u''
        crowdsourcing_answer_24.latitude = None
        crowdsourcing_answer_24.longitude = None
        crowdsourcing_answer_24.comment = u''
        crowdsourcing_answer_24.flickr_id = u''
        crowdsourcing_answer_24.photo_hash = None
        crowdsourcing_answer_24.save()

        crowdsourcing_answer_25 = Answer()
        crowdsourcing_answer_25.submission = crowdsourcing_submission_5
        crowdsourcing_answer_25.question = crowdsourcing_question_7
        crowdsourcing_answer_25.text_answer = u'favorable'
        crowdsourcing_answer_25.integer_answer = None
        crowdsourcing_answer_25.float_answer = None
        crowdsourcing_answer_25.boolean_answer = None
        crowdsourcing_answer_25.image_answer = u''
        crowdsourcing_answer_25.latitude = None
        crowdsourcing_answer_25.longitude = None
        crowdsourcing_answer_25.comment = u''
        crowdsourcing_answer_25.flickr_id = u''
        crowdsourcing_answer_25.photo_hash = None
        crowdsourcing_answer_25.save()

        crowdsourcing_answer_26 = Answer()
        crowdsourcing_answer_26.submission = crowdsourcing_submission_3
        crowdsourcing_answer_26.question = crowdsourcing_question_8
        crowdsourcing_answer_26.text_answer = u"J'ai une autre proposition (d\xe9taillez)"
        crowdsourcing_answer_26.integer_answer = None
        crowdsourcing_answer_26.float_answer = None
        crowdsourcing_answer_26.boolean_answer = None
        crowdsourcing_answer_26.image_answer = u''
        crowdsourcing_answer_26.latitude = None
        crowdsourcing_answer_26.longitude = None
        crowdsourcing_answer_26.comment = u"Faire appara\xeetre le nom de la structure \xe0 tous et pour le nom de l'utilisateur laisser le choix qu'il soit pr\xe9sent\xe9 ou non au non-inscrit"
        crowdsourcing_answer_26.flickr_id = u''
        crowdsourcing_answer_26.photo_hash = None
        crowdsourcing_answer_26.save()

        crowdsourcing_answer_27 = Answer()
        crowdsourcing_answer_27.submission = crowdsourcing_submission_2
        crowdsourcing_answer_27.question = crowdsourcing_question_7
        crowdsourcing_answer_27.text_answer = u'favorable'
        crowdsourcing_answer_27.integer_answer = None
        crowdsourcing_answer_27.float_answer = None
        crowdsourcing_answer_27.boolean_answer = None
        crowdsourcing_answer_27.image_answer = u''
        crowdsourcing_answer_27.latitude = None
        crowdsourcing_answer_27.longitude = None
        crowdsourcing_answer_27.comment = u''
        crowdsourcing_answer_27.flickr_id = u''
        crowdsourcing_answer_27.photo_hash = None
        crowdsourcing_answer_27.save()

        crowdsourcing_answer_28 = Answer()
        crowdsourcing_answer_28.submission = crowdsourcing_submission_1
        crowdsourcing_answer_28.question = crowdsourcing_question_8
        crowdsourcing_answer_28.text_answer = u"Oui, c'est un bon compromis"
        crowdsourcing_answer_28.integer_answer = None
        crowdsourcing_answer_28.float_answer = None
        crowdsourcing_answer_28.boolean_answer = None
        crowdsourcing_answer_28.image_answer = u''
        crowdsourcing_answer_28.latitude = None
        crowdsourcing_answer_28.longitude = None
        crowdsourcing_answer_28.comment = u''
        crowdsourcing_answer_28.flickr_id = u''
        crowdsourcing_answer_28.photo_hash = None
        crowdsourcing_answer_28.save()

        crowdsourcing_answer_29 = Answer()
        crowdsourcing_answer_29.submission = crowdsourcing_submission_5
        crowdsourcing_answer_29.question = crowdsourcing_question_10
        crowdsourcing_answer_29.text_answer = u'favorable'
        crowdsourcing_answer_29.integer_answer = None
        crowdsourcing_answer_29.float_answer = None
        crowdsourcing_answer_29.boolean_answer = None
        crowdsourcing_answer_29.image_answer = u''
        crowdsourcing_answer_29.latitude = None
        crowdsourcing_answer_29.longitude = None
        crowdsourcing_answer_29.comment = u''
        crowdsourcing_answer_29.flickr_id = u''
        crowdsourcing_answer_29.photo_hash = None
        crowdsourcing_answer_29.save()

        crowdsourcing_answer_30 = Answer()
        crowdsourcing_answer_30.submission = crowdsourcing_submission_4
        crowdsourcing_answer_30.question = crowdsourcing_question_10
        crowdsourcing_answer_30.text_answer = u'favorable'
        crowdsourcing_answer_30.integer_answer = None
        crowdsourcing_answer_30.float_answer = None
        crowdsourcing_answer_30.boolean_answer = None
        crowdsourcing_answer_30.image_answer = u''
        crowdsourcing_answer_30.latitude = None
        crowdsourcing_answer_30.longitude = None
        crowdsourcing_answer_30.comment = u''
        crowdsourcing_answer_30.flickr_id = u''
        crowdsourcing_answer_30.photo_hash = None
        crowdsourcing_answer_30.save()

        crowdsourcing_answer_31 = Answer()
        crowdsourcing_answer_31.submission = crowdsourcing_submission_3
        crowdsourcing_answer_31.question = crowdsourcing_question_9
        crowdsourcing_answer_31.text_answer = u'\xc7a devrait \xeatre optionnel'
        crowdsourcing_answer_31.integer_answer = None
        crowdsourcing_answer_31.float_answer = None
        crowdsourcing_answer_31.boolean_answer = None
        crowdsourcing_answer_31.image_answer = u''
        crowdsourcing_answer_31.latitude = None
        crowdsourcing_answer_31.longitude = None
        crowdsourcing_answer_31.comment = u"Le logo peut \xeatre un avatar car c'est un bon moyen d'identification"
        crowdsourcing_answer_31.flickr_id = u''
        crowdsourcing_answer_31.photo_hash = None
        crowdsourcing_answer_31.save()

        crowdsourcing_answer_32 = Answer()
        crowdsourcing_answer_32.submission = crowdsourcing_submission_6
        crowdsourcing_answer_32.question = crowdsourcing_question_9
        crowdsourcing_answer_32.text_answer = u'Utile et sympathique, il en faut'
        crowdsourcing_answer_32.integer_answer = None
        crowdsourcing_answer_32.float_answer = None
        crowdsourcing_answer_32.boolean_answer = None
        crowdsourcing_answer_32.image_answer = u''
        crowdsourcing_answer_32.latitude = None
        crowdsourcing_answer_32.longitude = None
        crowdsourcing_answer_32.comment = u''
        crowdsourcing_answer_32.flickr_id = u''
        crowdsourcing_answer_32.photo_hash = None
        crowdsourcing_answer_32.save()

        crowdsourcing_answer_33 = Answer()
        crowdsourcing_answer_33.submission = crowdsourcing_submission_2
        crowdsourcing_answer_33.question = crowdsourcing_question_10
        crowdsourcing_answer_33.text_answer = u'favorable'
        crowdsourcing_answer_33.integer_answer = None
        crowdsourcing_answer_33.float_answer = None
        crowdsourcing_answer_33.boolean_answer = None
        crowdsourcing_answer_33.image_answer = u''
        crowdsourcing_answer_33.latitude = None
        crowdsourcing_answer_33.longitude = None
        crowdsourcing_answer_33.comment = u''
        crowdsourcing_answer_33.flickr_id = u''
        crowdsourcing_answer_33.photo_hash = None
        crowdsourcing_answer_33.save()

        crowdsourcing_answer_34 = Answer()
        crowdsourcing_answer_34.submission = crowdsourcing_submission_7
        crowdsourcing_answer_34.question = crowdsourcing_question_10
        crowdsourcing_answer_34.text_answer = u'favorable'
        crowdsourcing_answer_34.integer_answer = None
        crowdsourcing_answer_34.float_answer = None
        crowdsourcing_answer_34.boolean_answer = None
        crowdsourcing_answer_34.image_answer = u''
        crowdsourcing_answer_34.latitude = None
        crowdsourcing_answer_34.longitude = None
        crowdsourcing_answer_34.comment = u''
        crowdsourcing_answer_34.flickr_id = u''
        crowdsourcing_answer_34.photo_hash = None
        crowdsourcing_answer_34.save()

        crowdsourcing_answer_35 = Answer()
        crowdsourcing_answer_35.submission = crowdsourcing_submission_1
        crowdsourcing_answer_35.question = crowdsourcing_question_9
        crowdsourcing_answer_35.text_answer = u'\xc7a devrait \xeatre optionnel'
        crowdsourcing_answer_35.integer_answer = None
        crowdsourcing_answer_35.float_answer = None
        crowdsourcing_answer_35.boolean_answer = None
        crowdsourcing_answer_35.image_answer = u''
        crowdsourcing_answer_35.latitude = None
        crowdsourcing_answer_35.longitude = None
        crowdsourcing_answer_35.comment = u''
        crowdsourcing_answer_35.flickr_id = u''
        crowdsourcing_answer_35.photo_hash = None
        crowdsourcing_answer_35.save()

        crowdsourcing_answer_36 = Answer()
        crowdsourcing_answer_36.submission = crowdsourcing_submission_6
        crowdsourcing_answer_36.question = crowdsourcing_question_11
        crowdsourcing_answer_36.text_answer = u'\xc7a peut \xeatre utile'
        crowdsourcing_answer_36.integer_answer = None
        crowdsourcing_answer_36.float_answer = None
        crowdsourcing_answer_36.boolean_answer = None
        crowdsourcing_answer_36.image_answer = u''
        crowdsourcing_answer_36.latitude = None
        crowdsourcing_answer_36.longitude = None
        crowdsourcing_answer_36.comment = u''
        crowdsourcing_answer_36.flickr_id = u''
        crowdsourcing_answer_36.photo_hash = None
        crowdsourcing_answer_36.save()

        crowdsourcing_answer_37 = Answer()
        crowdsourcing_answer_37.submission = crowdsourcing_submission_5
        crowdsourcing_answer_37.question = crowdsourcing_question_12
        crowdsourcing_answer_37.text_answer = u'favorable'
        crowdsourcing_answer_37.integer_answer = None
        crowdsourcing_answer_37.float_answer = None
        crowdsourcing_answer_37.boolean_answer = None
        crowdsourcing_answer_37.image_answer = u''
        crowdsourcing_answer_37.latitude = None
        crowdsourcing_answer_37.longitude = None
        crowdsourcing_answer_37.comment = u''
        crowdsourcing_answer_37.flickr_id = u''
        crowdsourcing_answer_37.photo_hash = None
        crowdsourcing_answer_37.save()

        crowdsourcing_answer_38 = Answer()
        crowdsourcing_answer_38.submission = crowdsourcing_submission_4
        crowdsourcing_answer_38.question = crowdsourcing_question_12
        crowdsourcing_answer_38.text_answer = u'\xe0 discuter'
        crowdsourcing_answer_38.integer_answer = None
        crowdsourcing_answer_38.float_answer = None
        crowdsourcing_answer_38.boolean_answer = None
        crowdsourcing_answer_38.image_answer = u''
        crowdsourcing_answer_38.latitude = None
        crowdsourcing_answer_38.longitude = None
        crowdsourcing_answer_38.comment = u"Cet outil devra \xeatre \xe9volutif en fonction des discussions qui pourraient \xeatre ouvertes \xe0 l'entr\xe9e de telle ou telle structure souhaitant amener d'autres crit\xe8res ou discuter sur la pertinence des crit\xe8res en place."
        crowdsourcing_answer_38.flickr_id = u''
        crowdsourcing_answer_38.photo_hash = None
        crowdsourcing_answer_38.save()

        crowdsourcing_answer_39 = Answer()
        crowdsourcing_answer_39.submission = crowdsourcing_submission_1
        crowdsourcing_answer_39.question = crowdsourcing_question_11
        crowdsourcing_answer_39.text_answer = u"Oui, mais il faut que \xe7a m'envoie les messages sur mon email aussi"
        crowdsourcing_answer_39.integer_answer = None
        crowdsourcing_answer_39.float_answer = None
        crowdsourcing_answer_39.boolean_answer = None
        crowdsourcing_answer_39.image_answer = u''
        crowdsourcing_answer_39.latitude = None
        crowdsourcing_answer_39.longitude = None
        crowdsourcing_answer_39.comment = u''
        crowdsourcing_answer_39.flickr_id = u''
        crowdsourcing_answer_39.photo_hash = None
        crowdsourcing_answer_39.save()

        crowdsourcing_answer_40 = Answer()
        crowdsourcing_answer_40.submission = crowdsourcing_submission_7
        crowdsourcing_answer_40.question = crowdsourcing_question_12
        crowdsourcing_answer_40.text_answer = u'favorable'
        crowdsourcing_answer_40.integer_answer = None
        crowdsourcing_answer_40.float_answer = None
        crowdsourcing_answer_40.boolean_answer = None
        crowdsourcing_answer_40.image_answer = u''
        crowdsourcing_answer_40.latitude = None
        crowdsourcing_answer_40.longitude = None
        crowdsourcing_answer_40.comment = u''
        crowdsourcing_answer_40.flickr_id = u''
        crowdsourcing_answer_40.photo_hash = None
        crowdsourcing_answer_40.save()

        crowdsourcing_answer_41 = Answer()
        crowdsourcing_answer_41.submission = crowdsourcing_submission_2
        crowdsourcing_answer_41.question = crowdsourcing_question_12
        crowdsourcing_answer_41.text_answer = u'favorable'
        crowdsourcing_answer_41.integer_answer = None
        crowdsourcing_answer_41.float_answer = None
        crowdsourcing_answer_41.boolean_answer = None
        crowdsourcing_answer_41.image_answer = u''
        crowdsourcing_answer_41.latitude = None
        crowdsourcing_answer_41.longitude = None
        crowdsourcing_answer_41.comment = u''
        crowdsourcing_answer_41.flickr_id = u''
        crowdsourcing_answer_41.photo_hash = None
        crowdsourcing_answer_41.save()

        crowdsourcing_answer_42 = Answer()
        crowdsourcing_answer_42.submission = crowdsourcing_submission_3
        crowdsourcing_answer_42.question = crowdsourcing_question_11
        crowdsourcing_answer_42.text_answer = u'\xc7a fait double emploi avec le courriel en g\xe9n\xe9ral, inutile'
        crowdsourcing_answer_42.integer_answer = None
        crowdsourcing_answer_42.float_answer = None
        crowdsourcing_answer_42.boolean_answer = None
        crowdsourcing_answer_42.image_answer = u''
        crowdsourcing_answer_42.latitude = None
        crowdsourcing_answer_42.longitude = None
        crowdsourcing_answer_42.comment = u''
        crowdsourcing_answer_42.flickr_id = u''
        crowdsourcing_answer_42.photo_hash = None
        crowdsourcing_answer_42.save()

        crowdsourcing_answer_43 = Answer()
        crowdsourcing_answer_43.submission = crowdsourcing_submission_6
        crowdsourcing_answer_43.question = crowdsourcing_question_13
        crowdsourcing_answer_43.text_answer = u'google Agenda'
        crowdsourcing_answer_43.integer_answer = None
        crowdsourcing_answer_43.float_answer = None
        crowdsourcing_answer_43.boolean_answer = None
        crowdsourcing_answer_43.image_answer = u''
        crowdsourcing_answer_43.latitude = None
        crowdsourcing_answer_43.longitude = None
        crowdsourcing_answer_43.comment = u''
        crowdsourcing_answer_43.flickr_id = u''
        crowdsourcing_answer_43.photo_hash = None
        crowdsourcing_answer_43.save()

        crowdsourcing_answer_44 = Answer()
        crowdsourcing_answer_44.submission = crowdsourcing_submission_6
        crowdsourcing_answer_44.question = crowdsourcing_question_13
        crowdsourcing_answer_44.text_answer = u'twitter'
        crowdsourcing_answer_44.integer_answer = None
        crowdsourcing_answer_44.float_answer = None
        crowdsourcing_answer_44.boolean_answer = None
        crowdsourcing_answer_44.image_answer = u''
        crowdsourcing_answer_44.latitude = None
        crowdsourcing_answer_44.longitude = None
        crowdsourcing_answer_44.comment = u''
        crowdsourcing_answer_44.flickr_id = u''
        crowdsourcing_answer_44.photo_hash = None
        crowdsourcing_answer_44.save()

        crowdsourcing_answer_45 = Answer()
        crowdsourcing_answer_45.submission = crowdsourcing_submission_1
        crowdsourcing_answer_45.question = crowdsourcing_question_13
        crowdsourcing_answer_45.text_answer = u'twitter'
        crowdsourcing_answer_45.integer_answer = None
        crowdsourcing_answer_45.float_answer = None
        crowdsourcing_answer_45.boolean_answer = None
        crowdsourcing_answer_45.image_answer = u''
        crowdsourcing_answer_45.latitude = None
        crowdsourcing_answer_45.longitude = None
        crowdsourcing_answer_45.comment = u'Il s\'agit d\'une question essentielle:\r\nPour moi ceux qui utilise d\xe9j\xe0 un r\xe9seau social "propri\xe9taire" pourraient pouvoir s\'en servir provisoirement mais il faut int\xe9grer et ou promouvoir des fonctionnalit\xe9s de r\xe9seaux sociaux en logiciels libres.\r\nEn terme de donn\xe9es il ne s\'agit pas simplement du code postal mais de l\'ensemble de ce qui est publi\xe9 qui peut \xeatre r\xe9cup\xe9r\xe9 automatiquement. Une forte possibilit\xe9 de filtrage doit \xeatre donn\xe9 au membre par rapport \xe0 un r\xe9seau social comme Facebook.'
        crowdsourcing_answer_45.flickr_id = u''
        crowdsourcing_answer_45.photo_hash = None
        crowdsourcing_answer_45.save()

        crowdsourcing_answer_46 = Answer()
        crowdsourcing_answer_46.submission = crowdsourcing_submission_3
        crowdsourcing_answer_46.question = crowdsourcing_question_13
        crowdsourcing_answer_46.text_answer = u'facebook'
        crowdsourcing_answer_46.integer_answer = None
        crowdsourcing_answer_46.float_answer = None
        crowdsourcing_answer_46.boolean_answer = None
        crowdsourcing_answer_46.image_answer = u''
        crowdsourcing_answer_46.latitude = None
        crowdsourcing_answer_46.longitude = None
        crowdsourcing_answer_46.comment = u''
        crowdsourcing_answer_46.flickr_id = u''
        crowdsourcing_answer_46.photo_hash = None
        crowdsourcing_answer_46.save()

        crowdsourcing_answer_47 = Answer()
        crowdsourcing_answer_47.submission = crowdsourcing_submission_3
        crowdsourcing_answer_47.question = crowdsourcing_question_13
        crowdsourcing_answer_47.text_answer = u'GMail'
        crowdsourcing_answer_47.integer_answer = None
        crowdsourcing_answer_47.float_answer = None
        crowdsourcing_answer_47.boolean_answer = None
        crowdsourcing_answer_47.image_answer = u''
        crowdsourcing_answer_47.latitude = None
        crowdsourcing_answer_47.longitude = None
        crowdsourcing_answer_47.comment = u''
        crowdsourcing_answer_47.flickr_id = u''
        crowdsourcing_answer_47.photo_hash = None
        crowdsourcing_answer_47.save()

        crowdsourcing_answer_48 = Answer()
        crowdsourcing_answer_48.submission = crowdsourcing_submission_1
        crowdsourcing_answer_48.question = crowdsourcing_question_13
        crowdsourcing_answer_48.text_answer = u'facebook'
        crowdsourcing_answer_48.integer_answer = None
        crowdsourcing_answer_48.float_answer = None
        crowdsourcing_answer_48.boolean_answer = None
        crowdsourcing_answer_48.image_answer = u''
        crowdsourcing_answer_48.latitude = None
        crowdsourcing_answer_48.longitude = None
        crowdsourcing_answer_48.comment = u'Il s\'agit d\'une question essentielle:\r\nPour moi ceux qui utilise d\xe9j\xe0 un r\xe9seau social "propri\xe9taire" pourraient pouvoir s\'en servir provisoirement mais il faut int\xe9grer et ou promouvoir des fonctionnalit\xe9s de r\xe9seaux sociaux en logiciels libres.\r\nEn terme de donn\xe9es il ne s\'agit pas simplement du code postal mais de l\'ensemble de ce qui est publi\xe9 qui peut \xeatre r\xe9cup\xe9r\xe9 automatiquement. Une forte possibilit\xe9 de filtrage doit \xeatre donn\xe9 au membre par rapport \xe0 un r\xe9seau social comme Facebook.'
        crowdsourcing_answer_48.flickr_id = u''
        crowdsourcing_answer_48.photo_hash = None
        crowdsourcing_answer_48.save()

        crowdsourcing_answer_49 = Answer()
        crowdsourcing_answer_49.submission = crowdsourcing_submission_2
        crowdsourcing_answer_49.question = crowdsourcing_question_14
        crowdsourcing_answer_49.text_answer = u'\xe0 discuter'
        crowdsourcing_answer_49.integer_answer = None
        crowdsourcing_answer_49.float_answer = None
        crowdsourcing_answer_49.boolean_answer = None
        crowdsourcing_answer_49.image_answer = u''
        crowdsourcing_answer_49.latitude = None
        crowdsourcing_answer_49.longitude = None
        crowdsourcing_answer_49.comment = u'Je ne comprend pas la notion de confidentialit\xe9 des \xe9changes. je m\'opposerais \xe0 toute forme de "soci\xe9t\xe9 secr\xe8te"'
        crowdsourcing_answer_49.flickr_id = u''
        crowdsourcing_answer_49.photo_hash = None
        crowdsourcing_answer_49.save()

        crowdsourcing_answer_50 = Answer()
        crowdsourcing_answer_50.submission = crowdsourcing_submission_6
        crowdsourcing_answer_50.question = crowdsourcing_question_13
        crowdsourcing_answer_50.text_answer = u'LinkedIn'
        crowdsourcing_answer_50.integer_answer = None
        crowdsourcing_answer_50.float_answer = None
        crowdsourcing_answer_50.boolean_answer = None
        crowdsourcing_answer_50.image_answer = u''
        crowdsourcing_answer_50.latitude = None
        crowdsourcing_answer_50.longitude = None
        crowdsourcing_answer_50.comment = u''
        crowdsourcing_answer_50.flickr_id = u''
        crowdsourcing_answer_50.photo_hash = None
        crowdsourcing_answer_50.save()

        crowdsourcing_answer_51 = Answer()
        crowdsourcing_answer_51.submission = crowdsourcing_submission_5
        crowdsourcing_answer_51.question = crowdsourcing_question_14
        crowdsourcing_answer_51.text_answer = u'favorable'
        crowdsourcing_answer_51.integer_answer = None
        crowdsourcing_answer_51.float_answer = None
        crowdsourcing_answer_51.boolean_answer = None
        crowdsourcing_answer_51.image_answer = u''
        crowdsourcing_answer_51.latitude = None
        crowdsourcing_answer_51.longitude = None
        crowdsourcing_answer_51.comment = u''
        crowdsourcing_answer_51.flickr_id = u''
        crowdsourcing_answer_51.photo_hash = None
        crowdsourcing_answer_51.save()

        crowdsourcing_answer_52 = Answer()
        crowdsourcing_answer_52.submission = crowdsourcing_submission_4
        crowdsourcing_answer_52.question = crowdsourcing_question_14
        crowdsourcing_answer_52.text_answer = u'favorable'
        crowdsourcing_answer_52.integer_answer = None
        crowdsourcing_answer_52.float_answer = None
        crowdsourcing_answer_52.boolean_answer = None
        crowdsourcing_answer_52.image_answer = u''
        crowdsourcing_answer_52.latitude = None
        crowdsourcing_answer_52.longitude = None
        crowdsourcing_answer_52.comment = u''
        crowdsourcing_answer_52.flickr_id = u''
        crowdsourcing_answer_52.photo_hash = None
        crowdsourcing_answer_52.save()

        crowdsourcing_answer_53 = Answer()
        crowdsourcing_answer_53.submission = crowdsourcing_submission_6
        crowdsourcing_answer_53.question = crowdsourcing_question_13
        crowdsourcing_answer_53.text_answer = u'google Documents'
        crowdsourcing_answer_53.integer_answer = None
        crowdsourcing_answer_53.float_answer = None
        crowdsourcing_answer_53.boolean_answer = None
        crowdsourcing_answer_53.image_answer = u''
        crowdsourcing_answer_53.latitude = None
        crowdsourcing_answer_53.longitude = None
        crowdsourcing_answer_53.comment = u''
        crowdsourcing_answer_53.flickr_id = u''
        crowdsourcing_answer_53.photo_hash = None
        crowdsourcing_answer_53.save()

        crowdsourcing_answer_54 = Answer()
        crowdsourcing_answer_54.submission = crowdsourcing_submission_7
        crowdsourcing_answer_54.question = crowdsourcing_question_14
        crowdsourcing_answer_54.text_answer = u'favorable'
        crowdsourcing_answer_54.integer_answer = None
        crowdsourcing_answer_54.float_answer = None
        crowdsourcing_answer_54.boolean_answer = None
        crowdsourcing_answer_54.image_answer = u''
        crowdsourcing_answer_54.latitude = None
        crowdsourcing_answer_54.longitude = None
        crowdsourcing_answer_54.comment = u''
        crowdsourcing_answer_54.flickr_id = u''
        crowdsourcing_answer_54.photo_hash = None
        crowdsourcing_answer_54.save()

        crowdsourcing_answer_55 = Answer()
        crowdsourcing_answer_55.submission = crowdsourcing_submission_2
        crowdsourcing_answer_55.question = crowdsourcing_question_15
        crowdsourcing_answer_55.text_answer = u'favorable'
        crowdsourcing_answer_55.integer_answer = None
        crowdsourcing_answer_55.float_answer = None
        crowdsourcing_answer_55.boolean_answer = None
        crowdsourcing_answer_55.image_answer = u''
        crowdsourcing_answer_55.latitude = None
        crowdsourcing_answer_55.longitude = None
        crowdsourcing_answer_55.comment = u''
        crowdsourcing_answer_55.flickr_id = u''
        crowdsourcing_answer_55.photo_hash = None
        crowdsourcing_answer_55.save()

        crowdsourcing_answer_56 = Answer()
        crowdsourcing_answer_56.submission = crowdsourcing_submission_4
        crowdsourcing_answer_56.question = crowdsourcing_question_15
        crowdsourcing_answer_56.text_answer = u'favorable'
        crowdsourcing_answer_56.integer_answer = None
        crowdsourcing_answer_56.float_answer = None
        crowdsourcing_answer_56.boolean_answer = None
        crowdsourcing_answer_56.image_answer = u''
        crowdsourcing_answer_56.latitude = None
        crowdsourcing_answer_56.longitude = None
        crowdsourcing_answer_56.comment = u''
        crowdsourcing_answer_56.flickr_id = u''
        crowdsourcing_answer_56.photo_hash = None
        crowdsourcing_answer_56.save()

        crowdsourcing_answer_57 = Answer()
        crowdsourcing_answer_57.submission = crowdsourcing_submission_5
        crowdsourcing_answer_57.question = crowdsourcing_question_15
        crowdsourcing_answer_57.text_answer = u'favorable'
        crowdsourcing_answer_57.integer_answer = None
        crowdsourcing_answer_57.float_answer = None
        crowdsourcing_answer_57.boolean_answer = None
        crowdsourcing_answer_57.image_answer = u''
        crowdsourcing_answer_57.latitude = None
        crowdsourcing_answer_57.longitude = None
        crowdsourcing_answer_57.comment = u"Je rajouterai bien qu'apr\xe8s cette p\xe9riode le collectif d\xe9cidera du mode de gestion du collectif et de la plate-forme."
        crowdsourcing_answer_57.flickr_id = u''
        crowdsourcing_answer_57.photo_hash = None
        crowdsourcing_answer_57.save()

        crowdsourcing_answer_58 = Answer()
        crowdsourcing_answer_58.submission = crowdsourcing_submission_7
        crowdsourcing_answer_58.question = crowdsourcing_question_15
        crowdsourcing_answer_58.text_answer = u'favorable'
        crowdsourcing_answer_58.integer_answer = None
        crowdsourcing_answer_58.float_answer = None
        crowdsourcing_answer_58.boolean_answer = None
        crowdsourcing_answer_58.image_answer = u''
        crowdsourcing_answer_58.latitude = None
        crowdsourcing_answer_58.longitude = None
        crowdsourcing_answer_58.comment = u''
        crowdsourcing_answer_58.flickr_id = u''
        crowdsourcing_answer_58.photo_hash = None
        crowdsourcing_answer_58.save()

        from crowdsourcing.models import SurveyReport





        chantiers_chantier_4.sondages.add(crowdsourcing_survey_2)

        chantiers_chantier_5.sondages.add(crowdsourcing_survey_1)

except Exception, e:
    raise e