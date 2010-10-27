# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Chantier'
        db.create_table('chantiers_chantier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modification', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=-1)),
        ))
        db.send_create_signal('chantiers', ['Chantier'])

        # Adding M2M table for field sondages on 'Chantier'
        db.create_table('chantiers_chantier_sondages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('chantier', models.ForeignKey(orm['chantiers.chantier'], null=False)),
            ('survey', models.ForeignKey(orm['crowdsourcing.survey'], null=False))
        ))
        db.create_unique('chantiers_chantier_sondages', ['chantier_id', 'survey_id'])


    def backwards(self, orm):
        
        # Deleting model 'Chantier'
        db.delete_table('chantiers_chantier')

        # Removing M2M table for field sondages on 'Chantier'
        db.delete_table('chantiers_chantier_sondages')


    models = {
        'chantiers.chantier': {
            'Meta': {'object_name': 'Chantier'},
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modification': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'sondages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['crowdsourcing.Survey']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'crowdsourcing.survey': {
            'Meta': {'ordering': "('-starts_at',)", 'unique_together': "(('survey_date', 'slug'),)", 'object_name': 'Survey'},
            'allow_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_multiple_submissions': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_voting': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'archive_policy': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'default_report': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'reports'", 'null': 'True', 'to': "orm['crowdsourcing.SurveyReport']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ends_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'flickr_group_id': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'flickr_group_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'moderate_submissions': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'require_login': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'starts_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'survey_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'tease': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'thanks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'crowdsourcing.surveyreport': {
            'Meta': {'ordering': "('title',)", 'unique_together': "(('survey', 'slug'),)", 'object_name': 'SurveyReport'},
            'display_individual_results': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'display_the_filters': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limit_results_to': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sort_by_rating': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['crowdsourcing.Survey']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        },
        'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_tagged_items'", 'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggit_taggeditem_items'", 'to': "orm['taggit.Tag']"})
        }
    }

    complete_apps = ['chantiers']
