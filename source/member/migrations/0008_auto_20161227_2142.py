# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_auto_20160605_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='theme',
            field=models.CharField(choices=[('leopro', 'Leopro'), ('standard', 'Standard')], default=None, max_length=16, blank=True, null=True),
        ),
    ]
