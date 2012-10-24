# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table('baseinfo_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='childpoint', null=True, to=orm['baseinfo.Place'])),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('parent_title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pinyin', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('zimu', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('id_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('hot', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('have_scene', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('extra', self.gf('django.db.models.fields.CharField')(default=u'0000000000000000', max_length=16, null=True, blank=True)),
        ))
        db.send_create_signal('baseinfo', ['Place'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table('baseinfo_place')


    models = {
        'baseinfo.place': {
            'Meta': {'object_name': 'Place'},
            'extra': ('django.db.models.fields.CharField', [], {'default': "u'0000000000000000'", 'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'have_scene': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'hot': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'childpoint'", 'null': 'True', 'to': "orm['baseinfo.Place']"}),
            'parent_title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pinyin': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zimu': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['baseinfo']