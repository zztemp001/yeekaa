# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Place.parent_title'
        db.alter_column('baseinfo_place', 'parent_title', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Place.pinyin'
        db.alter_column('baseinfo_place', 'pinyin', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Place.id_code'
        db.alter_column('baseinfo_place', 'id_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'Place.zimu'
        db.alter_column('baseinfo_place', 'zimu', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

    def backwards(self, orm):

        # Changing field 'Place.parent_title'
        db.alter_column('baseinfo_place', 'parent_title', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Place.pinyin'
        db.alter_column('baseinfo_place', 'pinyin', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Place.id_code'
        db.alter_column('baseinfo_place', 'id_code', self.gf('django.db.models.fields.CharField')(default='', max_length=10))

        # Changing field 'Place.zimu'
        db.alter_column('baseinfo_place', 'zimu', self.gf('django.db.models.fields.CharField')(default='', max_length=20))

    models = {
        'baseinfo.place': {
            'Meta': {'object_name': 'Place'},
            'extra': ('django.db.models.fields.CharField', [], {'default': "u'0000000000000000'", 'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'have_scene': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'hot': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'childpoint'", 'null': 'True', 'to': "orm['baseinfo.Place']"}),
            'parent_title': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pinyin': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zimu': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'})
        }
    }

    complete_apps = ['baseinfo']