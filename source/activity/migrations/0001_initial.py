# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('start', models.DateTimeField(blank=True, verbose_name='start', null=True)),
                ('end', models.DateTimeField(blank=True, verbose_name='end', null=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('member_cost', models.DecimalField(max_digits=8, help_text='Cost for attending this event', decimal_places=2)),
                ('outsider_allowed', models.BooleanField(default=True, help_text='Are non-members welcome at this event?')),
                ('outsider_cost', models.DecimalField(max_digits=8, help_text='Cost for attending this event if you are not a member', decimal_places=2)),
                ('registration_mode', models.CharField(choices=[('no', 'No registration'), ('possible', 'Registration possible'), ('suggested', 'Registration suggested'), ('required', 'Registration required')], help_text='Do visitors register?', max_length=12)),
                ('registration_deadline', models.DateTimeField(blank=True, help_text='After which time does registration close?', null=True)),
            ],
            options={
                'verbose_name_plural': 'activities',
                'verbose_name': 'activity',
            },
        ),
    ]
