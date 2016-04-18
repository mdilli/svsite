# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawHtmlModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, parent_link=True, to='cms.CMSPlugin', auto_created=True)),
                ('body', models.TextField(verbose_name='HTML')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
