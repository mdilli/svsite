# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_auto_20160323_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='theme',
            field=models.CharField(choices=[('leopro', 'Leopro'), ('standard', 'Standard')], default=None, max_length=16, null=True, blank=True),
        ),
    ]
