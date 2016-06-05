# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0013_urlconfrevision'),
        ('tweaks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMSMember',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(default='Members', max_length=64)),
                ('description', models.TextField(blank=True)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
