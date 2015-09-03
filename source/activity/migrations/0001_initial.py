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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('member_cost', models.DecimalField(decimal_places=2, help_text='Cost for attending this event', max_digits=8)),
                ('outsider_allowed', models.BooleanField(help_text='Are non-members welcome at this event?', default=True)),
                ('outsider_cost', models.DecimalField(decimal_places=2, help_text='Cost for attending this event if you are not a member', max_digits=8)),
                ('registration_mode', models.CharField(help_text='Do visitors register?', max_length=12, choices=[('no', 'No registration'), ('possible', 'Registration possible'), ('suggested', 'Registration suggested'), ('required', 'Registration required')])),
                ('registration_deadline', models.DateTimeField(blank=True, help_text='After which time does registration close?', null=True)),
            ],
            options={
                'verbose_name': 'activity',
                'verbose_name_plural': 'activities',
            },
        ),
    ]
