# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BadgeAward',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_created=True)),
                ('badge', models.CharField(max_length=8, choices=[('soatt', 'Sword of a Thousand Truths')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='badges_awarded')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='badgeaward',
            unique_together=set([('user', 'badge')]),
        ),
    ]
