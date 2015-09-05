# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20150904_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='system',
            field=models.BooleanField(help_text='System teams are essential and cannot be changed', default=False),
        ),
        migrations.AlterField(
            model_name='team',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, help_text='This value is used as identifier in places like urls.', unique=True, populate_from='name', editable=False),
        ),
    ]
