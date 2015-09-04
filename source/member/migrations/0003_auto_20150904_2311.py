# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import svsite.models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20150904_2236'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='member',
            managers=[
                ('objects', svsite.models.UserPermissionManager()),
            ],
        ),
    ]
