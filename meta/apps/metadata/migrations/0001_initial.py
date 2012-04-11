# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Institution'
        db.create_table('metadata_institution', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('realm', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
            ('org_name_se', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('org_name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('info_url_se', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('info_url_en', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('policy_url_se', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('policy_url_en', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('metadata', ['Institution'])

        # Adding model 'Contact'
        db.create_table('metadata_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['metadata.Institution'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('metadata', ['Contact'])

        # Adding model 'Location'
        db.create_table('metadata_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['metadata.Institution'])),
            ('location_name_se', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('location_name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('location_shortname', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('ssid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('enc_level', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('port_restrict', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('transp_proxy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ipv6', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nat', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ap_no', self.gf('django.db.models.fields.IntegerField')()),
            ('wired', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('info_url_se', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('info_url_en', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('metadata', ['Location'])


    def backwards(self, orm):
        
        # Deleting model 'Institution'
        db.delete_table('metadata_institution')

        # Deleting model 'Contact'
        db.delete_table('metadata_contact')

        # Deleting model 'Location'
        db.delete_table('metadata_location')


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
            'area': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
