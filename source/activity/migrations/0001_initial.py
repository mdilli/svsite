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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('start', models.DateTimeField(null=True, help_text='When does the event start?', blank=True)),
                ('end', models.DateTimeField(null=True, help_text='When does the event end?', blank=True)),
                ('member_cost', models.DecimalField(help_text='Cost for attending this event', max_digits=8, decimal_places=2)),
                ('outsider_allowed', models.BooleanField(help_text='Are non-members welcome at this event?', default=True)),
                ('outsider_cost', models.DecimalField(help_text='Cost for attending this event if you are not a member', max_digits=8, decimal_places=2)),
                ('registration_mode', models.CharField(choices=[('no', 'No registration'), ('possible', 'Registration possible'), ('suggested', 'Registration suggested'), ('required', 'Registration required')], help_text='Do visitors register?', max_length=12)),
                ('registration_deadline', models.DateTimeField(null=True, help_text='After which time does registration close?', blank=True)),
            ],
        ),
    ]
