# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.SlugField(error_messages={'unique': 'A user with that username already exists.'}, unique=True)),
                ('listed', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, default='')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('admin', models.BooleanField(help_text='Admins can and and remove members and update descriptions', default=False)),
                ('role', models.CharField(blank=True, default='', max_length=64)),
                ('member', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(to='teams.Team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(blank=True, through='teams.TeamMember', to=settings.AUTH_USER_MODEL),
        ),
    ]
