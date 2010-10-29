# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'OrganismeLocal'
        db.create_table('local_organismelocal', (
            ('organisme_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['organisme.Organisme'], unique=True, primary_key=True)),
            ('fse', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('local', ['OrganismeLocal'])

        # Adding model 'Relation'
        db.create_table('local_relation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('auteur', self.gf('django.db.models.fields.related.ForeignKey')(related_name='auteur_related', to=orm['local.OrganismeLocal'])),
            ('cible', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cible_related', to=orm['local.OrganismeLocal'])),
            ('type_relation', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('date_crea', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modif', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('local', ['Relation'])


    def backwards(self, orm):
        
        # Deleting model 'OrganismeLocal'
        db.delete_table('local_organismelocal')

        # Deleting model 'Relation'
        db.delete_table('local_relation')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'local.organismelocal': {
            'Meta': {'ordering': "['nom']", 'object_name': 'OrganismeLocal', '_ormbases': ['organisme.Organisme']},
            'fse': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'organisme_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['organisme.Organisme']", 'unique': 'True', 'primary_key': 'True'}),
            'relations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['local.OrganismeLocal']", 'through': "orm['local.Relation']", 'symmetrical': 'False'})
        },
        'local.relation': {
            'Meta': {'object_name': 'Relation'},
            'auteur': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'auteur_related'", 'to': "orm['local.OrganismeLocal']"}),
            'cible': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cible_related'", 'to': "orm['local.OrganismeLocal']"}),
            'date_crea': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modif': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_relation': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'organisme.organisme': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Organisme'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'auteur': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'code_postal': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modification': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'reseau': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sigle': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        }
    }

    complete_apps = ['local']
