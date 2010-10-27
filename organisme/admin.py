# -*- coding:utf-8 -*-
from django.contrib import admin
from organisme.models import Organisme
from organisme.models import Relation


class RelationInline(admin.TabularInline):
	model = Relation
	fk_name = 'auteur'
	raw_id_fields = ('cible',)
	extra = 1

class OrganismeAdmin(admin.ModelAdmin):
	#save_on_top = True
	actions_on_bottom = True
	actions_on_top = False
	search_fields = ('nom','sigle')	
	list_display = ('nom','code_postal','ville','reseau')
	#faire un callable qui met le sigle ou le nom
	prepopulated_fields = {'slug':('nom',)}
	fieldsets = (
		(u'Coordonnées', {
			'fields':('nom','sigle','adresse','code_postal','ville','telephone','email','url')
		}),
		
		#(u'Relations', {'fields':('relations',)}),
		
		(u'Options', {
			'description':'<b>A ne modifier que si vous savez ce que vous faites...</b>',
			'classes':('collapse',),
			'fields':('reseau','actif','slug','auteur')
		}),
	)
	inlines = (RelationInline,)
	

	
admin.site.register(Organisme,OrganismeAdmin)
