# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ContactType'
        db.delete_table(u'members_contacttype')

        # Deleting field 'Contact.contact_type'
        db.delete_column(u'members_contact', 'contact_type_id')


    def backwards(self, orm):
        # Adding model 'ContactType'
        db.create_table(u'members_contacttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'members', ['ContactType'])


        # User chose to not deal with backwards NULL issues for 'Contact.contact_type'
        raise RuntimeError("Cannot reverse this migration. 'Contact.contact_type' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Contact.contact_type'
        db.add_column(u'members_contact', 'contact_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.ContactType']),
                      keep_default=False)


    models = {
        u'members.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Hrvatska'", 'max_length': '32', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.Member']"}),
            'town': ('django.db.models.fields.CharField', [], {'default': "'Zagreb'", 'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'default': "'10000'", 'max_length': '16', 'null': 'True', 'blank': 'True'})
        },
        u'members.contact': {
            'Meta': {'object_name': 'Contact'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'contact_type_char': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.Member']"})
        },
        u'members.group': {
            'Meta': {'object_name': 'Group'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.Group']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'members.member': {
            'Meta': {'object_name': 'Member'},
            'birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'card_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'comment': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'death': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['members.Group']", 'through': u"orm['members.MemberGroupLink']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        u'members.membergrouplink': {
            'Meta': {'object_name': 'MemberGroupLink'},
            'date_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['members.Member']"})
        }
    }

    complete_apps = ['members']