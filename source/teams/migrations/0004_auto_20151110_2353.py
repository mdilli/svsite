# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_auto_20151110_2353'),
        ('member', '0005_remove_member_teams'),
        ('teams', '0003_auto_20150905_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='members',
        ),
        migrations.AlterUniqueTogether(
            name='teammember',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='member',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='team',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.DeleteModel(
            name='TeamMember',
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
            ],
            options={
                'verbose_name': 'Team',
                'proxy': True,
                'verbose_name_plural': 'Teams',
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]
