# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='BirthdaysPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', serialize=False, auto_created=True, primary_key=True, parent_link=True)),
                ('caption', models.CharField(max_length=32, default='Happy birthday to...')),
                ('max_days', models.PositiveSmallIntegerField(null=True, blank=True, validators=[django.core.validators.MaxValueValidator(365)], default=7)),
                ('max_entries', models.PositiveSmallIntegerField(null=True, blank=True, default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
