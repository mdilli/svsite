# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('teams', '0002_auto_20150903_2252'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='team',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='team',
            name='id',
        ),
        migrations.RemoveField(
            model_name='team',
            name='members',
        ),
        migrations.RemoveField(
            model_name='team',
            name='name',
        ),
        migrations.RemoveField(
            model_name='team',
            name='permissions',
        ),
        migrations.AddField(
            model_name='team',
            name='group_ptr',
            field=models.OneToOneField(default=None, to='auth.Group', primary_key=True, auto_created=True, parent_link=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teammember',
            name='team',
            field=models.ForeignKey(to='auth.Group'),
        ),
    ]
