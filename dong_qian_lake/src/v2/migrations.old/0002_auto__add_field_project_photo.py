# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.photo'
        db.add_column('mysite_project', 'photo',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.photo'
        db.delete_column('mysite_project', 'photo')


    models = {
        'mysite.project': {
            'Meta': {'object_name': 'Project'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'build_unit': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'completed_invest': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'blank': 'True'}),
            'completed_time': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'funds_source': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invest_subject': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'leader': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'no': ('django.db.models.fields.IntegerField', [], {}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'planed_invest': ('django.db.models.fields.BigIntegerField', [], {'default': '0', 'blank': 'True'}),
            'problem': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'project_information': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project_schedule': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'project_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'remark': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'start_time': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'total_invest': ('django.db.models.fields.BigIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['mysite']