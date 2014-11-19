# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ThumbnailOption'
        db.create_table(u'ckeditor_filer_thumbnailoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('width', self.gf('django.db.models.fields.IntegerField')()),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
            ('crop', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('upscale', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('ckeditor_filer', ['ThumbnailOption'])


    def backwards(self, orm):
        # Deleting model 'ThumbnailOption'
        db.delete_table(u'ckeditor_filer_thumbnailoption')


    models = {
        'ckeditor_filer.thumbnailoption': {
            'Meta': {'ordering': "('width', 'height')", 'object_name': 'ThumbnailOption'},
            'crop': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'upscale': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['ckeditor_filer']