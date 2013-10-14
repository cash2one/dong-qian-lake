# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ProjectProgress.photo'
        db.delete_column('mysite_projectprogress', 'photo')

        # Adding field 'ProjectProgress.photo1'
        db.add_column('mysite_projectprogress', 'photo1',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ProjectProgress.photo2'
        db.add_column('mysite_projectprogress', 'photo2',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ProjectProgress.photo3'
        db.add_column('mysite_projectprogress', 'photo3',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ProjectProgress.photo4'
        db.add_column('mysite_projectprogress', 'photo4',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ProjectProgress.photo5'
        db.add_column('mysite_projectprogress', 'photo5',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ProjectProgress.photo'
        db.add_column('mysite_projectprogress', 'photo',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'ProjectProgress.photo1'
        db.delete_column('mysite_projectprogress', 'photo1')

        # Deleting field 'ProjectProgress.photo2'
        db.delete_column('mysite_projectprogress', 'photo2')

        # Deleting field 'ProjectProgress.photo3'
        db.delete_column('mysite_projectprogress', 'photo3')

        # Deleting field 'ProjectProgress.photo4'
        db.delete_column('mysite_projectprogress', 'photo4')

        # Deleting field 'ProjectProgress.photo5'
        db.delete_column('mysite_projectprogress', 'photo5')


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
            'month': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo1': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo2': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo4': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo5': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'problem': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'progress': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mysite.ProjectOverView']"}),
            'remark': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'responsible_for': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'year': ('django.db.models.fields.CharField', [], {'default': "'2013'", 'max_length': '10'})
        }
    }

    complete_apps = ['mysite']