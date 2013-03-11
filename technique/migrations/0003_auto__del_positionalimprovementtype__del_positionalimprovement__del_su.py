# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PositionalImprovementType'
        db.delete_table('technique_positionalimprovementtype')

        # Deleting model 'PositionalImprovement'
        db.delete_table('technique_positionalimprovement')

        # Deleting model 'Submission'
        db.delete_table('technique_submission')

        # Deleting model 'SubmissionType'
        db.delete_table('technique_submissiontype')

        # Deleting model 'Position'
        db.delete_table('technique_position')

        # Adding model 'Technique'
        db.create_table('technique_technique', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['technique.Level'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['technique.TechniqueType'])),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('start', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='starting_at', null=True, to=orm['technique.Technique'])),
            ('end', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='ending_at', null=True, to=orm['technique.Technique'])),
            ('youtube_id', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('youtube_link', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('youtube_start', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('technique', ['Technique'])

        # Adding model 'TechniqueType'
        db.create_table('technique_techniquetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('technique', ['TechniqueType'])


    def backwards(self, orm):
        # Adding model 'PositionalImprovementType'
        db.create_table('technique_positionalimprovementtype', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal('technique', ['PositionalImprovementType'])

        # Adding model 'PositionalImprovement'
        db.create_table('technique_positionalimprovement', (
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('youtube_link', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('end', self.gf('django.db.models.fields.related.ForeignKey')(related_name='end_pis', to=orm['technique.Position'])),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['technique.Level'])),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('start', self.gf('django.db.models.fields.related.ForeignKey')(related_name='start_pis', to=orm['technique.Position'])),
            ('youtube_id', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('youtube_start', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['technique.PositionalImprovementType'])),
        ))
        db.send_create_signal('technique', ['PositionalImprovement'])

        # Adding model 'Submission'
        db.create_table('technique_submission', (
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('youtube_link', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['technique.Level'])),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('start', self.gf('django.db.models.fields.related.ForeignKey')(related_name='start_submission', to=orm['technique.Position'])),
            ('youtube_id', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('youtube_start', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('technique', ['Submission'])

        # Adding model 'SubmissionType'
        db.create_table('technique_submissiontype', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['technique.SubmissionType'], null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('technique', ['SubmissionType'])

        # Adding model 'Position'
        db.create_table('technique_position', (
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('youtube_link', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['technique.Level'])),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('youtube_id', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('youtube_start', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('technique', ['Position'])

        # Deleting model 'Technique'
        db.delete_table('technique_technique')

        # Deleting model 'TechniqueType'
        db.delete_table('technique_techniquetype')


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
        'technique.level': {
            'Meta': {'ordering': "('pk',)", 'object_name': 'Level'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'technique.technique': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Technique'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ending_at'", 'null': 'True', 'to': "orm['technique.Technique']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['technique.Level']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'start': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'starting_at'", 'null': 'True', 'to': "orm['technique.Technique']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['technique.TechniqueType']"}),
            'youtube_id': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'youtube_link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'youtube_start': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'technique.techniquetype': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'TechniqueType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['technique']