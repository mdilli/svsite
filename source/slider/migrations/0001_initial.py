# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('weight', models.PositiveSmallIntegerField(help_text='How likely is this image to show up?', default=1)),
                ('image', django_resized.forms.ResizedImageField(upload_to='slider', help_text='Images should be at least 1600x150, or they will be scaled up, reducing quality.')),
            ],
        ),
    ]
