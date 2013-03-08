# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Position'
        db.create_table('technique_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['technique.Level'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('youtube_id', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('youtube_link', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('youtube_start', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('technique', ['Position'])

        # Adding model 'Submission'
        db.create_table('technique_submission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['technique.Level'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('youtube_id', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('youtube_link', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('youtube_start', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('start', self.gf('django.db.models.fields.related.ForeignKey')(related_name='start_submission', to=orm['technique.Position'])),
        ))
        db.send_create_signal('technique', ['Submission'])

        # Adding model 'SubmissionType'
        db.create_table('technique_submissiontype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['technique.SubmissionType'], null=True, blank=True)),
        ))
        db.send_create_signal('technique', ['SubmissionType'])

        # Adding model 'PositionalImprovement'
        db.create_table('technique_positionalimprovement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['technique.Level'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('youtube_id', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('youtube_link', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('youtube_start', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['technique.PositionalImprovementType'])),
            ('start', self.gf('django.db.models.fields.related.ForeignKey')(related_name='start_pis', to=orm['technique.Position'])),
            ('end', self.gf('django.db.models.fields.related.ForeignKey')(related_name='end_pis', to=orm['technique.Position'])),
        ))
        db.send_create_signal('technique', ['PositionalImprovement'])

        # Adding model 'PositionalImprovementType'
        db.create_table('technique_positionalimprovementtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('technique', ['PositionalImprovementType'])

        # Adding model 'Level'
        db.create_table('technique_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('technique', ['Level'])


    def backwards(self, orm):
        # Deleting model 'Position'
        db.delete_table('technique_position')

        # Deleting model 'Submission'
        db.delete_table('technique_submission')

        # Deleting model 'SubmissionType'
        db.delete_table('technique_submissiontype')

        # Deleting model 'PositionalImprovement'
        db.delete_table('technique_positionalimprovement')

        # Deleting model 'PositionalImprovementType'
        db.delete_table('technique_positionalimprovementtype')

        # Deleting model 'Level'
        db.delete_table('technique_level')


    models = {
        'technique.level': {
            'Meta': {'ordering': "('pk',)", 'object_name': 'Level'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'technique.position': {
            'Meta': {'object_name': 'Position'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['technique.Level']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'youtube_link': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'youtube_start': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'technique.positionalimprovement': {
            'Meta': {'object_name': 'PositionalImprovement'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'end_pis'", 'to': "orm['technique.Position']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['technique.Level']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'start': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'start_pis'", 'to': "orm['technique.Position']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['technique.PositionalImprovementType']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'youtube_link': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'youtube_start': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'technique.positionalimprovementtype': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'PositionalImprovementType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'technique.submission': {
            'Meta': {'object_name': 'Submission'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['technique.Level']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'start': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'start_submission'", 'to': "orm['technique.Position']"}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'youtube_link': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'youtube_start': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'technique.submissiontype': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'SubmissionType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['technique.SubmissionType']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['technique']