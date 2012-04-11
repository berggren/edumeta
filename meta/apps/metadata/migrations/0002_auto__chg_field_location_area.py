# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Location.area'
        db.alter_column('metadata_location', 'area', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))


    def backwards(self, orm):
        
        # Changing field 'Location.area'
        db.alter_column('metadata_location', 'area', self.gf('django.db.models.fields.TextField')(null=True))


    models = {
        'metadata.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['metadata.Institution']"}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'metadata.institution': {
            'Meta': {'object_name': 'Institution'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_url_en': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'info_url_se': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'org_name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'org_name_se': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'policy_url_en': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'policy_url_se': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'realm': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        'metadata.location': {
            'Meta': {'object_name': 'Location'},
            'ap_no': ('django.db.models.fields.IntegerField', [], {}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'enc_level': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info_url_en': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'info_url_se': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['metadata.Institution']"}),
            'ipv6': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'location_name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'location_name_se': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'location_shortname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'port_restrict': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ssid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'transp_proxy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wired': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['metadata']
