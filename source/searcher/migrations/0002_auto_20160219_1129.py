# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchresults',
            name='placeholder',
        ),
        migrations.AlterUniqueTogether(
            name='searchresultstranslation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='searchresultstranslation',
            name='master',
        ),
        migrations.DeleteModel(
            name='SearchResults',
        ),
        migrations.DeleteModel(
            name='SearchResultsTranslation',
        ),
    ]
