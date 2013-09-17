# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProjectOverView'
        db.create_table('mysite_projectoverview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('project_content', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('year_limit', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('planed_invest', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('year_content', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('response_for', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal('mysite', ['ProjectOverView'])


        # Changing field 'ProjectProgress.project'
        db.alter_column('mysite_projectprogress', 'project_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mysite.ProjectOverView']))

    def backwards(self, orm):
        # Deleting model 'ProjectOverView'
        db.delete_table('mysite_projectoverview')


        # Changing field 'ProjectProgress.project'
        db.alter_column('mysite_projectprogress', 'project_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mysite.Project']))

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
        },
        'mysite.projectoverview': {
            'Meta': {'object_name': 'ProjectOverView'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'planed_invest': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'project_content': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'response_for': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'year_content': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'year_limit': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        'mysite.projectprogress': {
            'Meta': {'object_name': 'ProjectProgress'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invest': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'month': ('django.db.models.fields.IntegerField', [], {'default': "'1'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'problem': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'progress': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mysite.ProjectOverView']"}),
            'remark': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'responsible_for': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'year': ('django.db.models.fields.CharField', [], {'default': "'2013'", 'max_length': '10'})
        }
    }

    complete_apps = ['mysite']