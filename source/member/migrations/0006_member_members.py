# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_auto_20151110_2353'),
        ('member', '0005_remove_member_teams'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='members',
            field=models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', verbose_name='groups', blank=True),
        ),
    ]
