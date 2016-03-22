# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sortedm2m.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20160203_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamAdmin',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('member', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(to='member.Team')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeamRole',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('role', models.TextField(blank=True, default='')),
                ('member', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(to='member.Team')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='team',
            name='admins',
            field=models.ManyToManyField(related_name='admin_teams', through='member.TeamAdmin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='roles',
            field=sortedm2m.fields.SortedManyToManyField(related_name='team_roles', help_text=None, through='member.TeamRole', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='teamrole',
            unique_together=set([('member', 'team')]),
        ),
        migrations.AlterUniqueTogether(
            name='teamadmin',
            unique_together=set([('member', 'team')]),
        ),
    ]
