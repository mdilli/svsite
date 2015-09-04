# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(error_messages={'unique': 'A team with that name already exists.'}, unique=True, max_length=48)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, populate_from='name', editable=False, unique=True)),
                ('listed', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, default='')),
                ('permission_census', models.BooleanField(default=False)),
                ('permission_full_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Teams',
                'verbose_name': 'Team',
            },
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('admin', models.BooleanField(default=False, help_text='Admins can and and remove members and update descriptions')),
                ('role', models.CharField(blank=True, default='', max_length=64)),
                ('member', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(to='teams.Team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, through='teams.TeamMember'),
        ),
        migrations.AlterUniqueTogether(
            name='teammember',
            unique_together=set([('member', 'team')]),
        ),
    ]
