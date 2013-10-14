# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ProjectOverView.name'
        db.delete_column('mysite_projectoverview', 'name')

        # Adding field 'ProjectOverView.project_name'
        db.add_column('mysite_projectoverview', 'project_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'ProjectOverView.project_schedule'
        db.add_column('mysite_projectoverview', 'project_schedule',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Adding field 'ProjectOverView.invest_subject'
        db.add_column('mysite_projectoverview', 'invest_subject',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Adding field 'ProjectOverView.start_time'
        db.add_column('mysite_projectoverview', 'start_time',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'ProjectOverView.completed_time'
        db.add_column('mysite_projectoverview', 'completed_time',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ProjectOverView.name'
        db.add_column('mysite_projectoverview', 'name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Deleting field 'ProjectOverView.project_name'
        db.delete_column('mysite_projectoverview', 'project_name')

        # Deleting field 'ProjectOverView.project_schedule'
        db.delete_column('mysite_projectoverview', 'project_schedule')

        # Deleting field 'ProjectOverView.invest_subject'
        db.delete_column('mysite_projectoverview', 'invest_subject')

        # Deleting field 'ProjectOverView.start_time'
        db.delete_column('mysite_projectoverview', 'start_time')

        # Deleting field 'ProjectOverView.completed_time'
        db.delete_column('mysite_projectoverview', 'completed_time')


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
            'completed_time': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invest_subject': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'planed_invest': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'project_content': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'project_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project_schedule': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'response_for': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
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