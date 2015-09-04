# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('teams', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='teams',
            field=models.ManyToManyField(blank=True, to='teams.Team', through='teams.TeamMember'),
        ),
        migrations.AddField(
            model_name='member',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, verbose_name='user permissions', related_query_name='user', related_name='user_set', to='auth.Permission', help_text='Specific permissions for this user.'),
        ),
    ]
