# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_member_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='groups',
            field=models.ManyToManyField(through='teams.TeamMember', blank=True, to='auth.Group'),
        ),
    ]
