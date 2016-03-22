# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20160317_1511'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teamrole',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='teamrole',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='roles',
            field=models.ManyToManyField(through='member.TeamRole', to=settings.AUTH_USER_MODEL, related_name='team_roles'),
        ),
        migrations.AlterUniqueTogether(
            name='teamrole',
            unique_together=set([]),
        ),
    ]
