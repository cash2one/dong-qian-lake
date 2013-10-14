# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('mysite_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('invest_subject', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('project_schedule', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('no', self.gf('django.db.models.fields.IntegerField')()),
            ('project_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('project_type', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('total_invest', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('planed_invest', self.gf('django.db.models.fields.BigIntegerField')(default=0, blank=True)),
            ('completed_invest', self.gf('django.db.models.fields.BigIntegerField')(default=0, blank=True)),
            ('funds_source', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('start_time', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('completed_time', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('leader', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('build_unit', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('project_information', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('problem', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('remark', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('mysite', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('mysite_project')


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