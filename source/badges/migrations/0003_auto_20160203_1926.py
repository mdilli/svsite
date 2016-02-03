# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0002_auto_20160130_2300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='badgeaward',
            options={'ordering': ('-pk',)},
        ),
        migrations.AlterField(
            model_name='badgeaward',
            name='badge',
            field=models.CharField(choices=[('soatt', 'The Sword of a Thousand Truths')], max_length=8),
        ),
    ]
