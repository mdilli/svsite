# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='team',
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='permissions',
            field=models.ManyToManyField(to='auth.Permission', blank=True),
        ),
    ]
