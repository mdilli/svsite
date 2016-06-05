# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_member_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='theme',
            field=models.CharField(blank=True, max_length=16, default=None, null=True, choices=[('standard', 'Standard'), ('leopro', 'Leopro')]),
        ),
    ]
