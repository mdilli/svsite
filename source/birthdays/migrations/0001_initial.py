# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='BirthdaysPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, to='cms.CMSPlugin', primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=32, default='Happy birthday to...')),
                ('max_days', models.PositiveSmallIntegerField(default=7, null=True, blank=True, validators=[django.core.validators.MaxValueValidator(365)])),
                ('max_entries', models.PositiveSmallIntegerField(null=True, blank=True, default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
