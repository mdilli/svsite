# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20150904_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='birthday',
            field=models.DateField(null=True, blank=True, default=None),
        ),
    ]
