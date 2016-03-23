# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20160317_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teamrole',
            old_name='role',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='teamrole',
            name='order',
            field=models.PositiveIntegerField(editable=False, db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name='teamrole',
            unique_together=set([('member', 'team')]),
        ),
    ]
