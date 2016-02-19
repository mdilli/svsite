# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchResults',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('placeholder', cms.models.fields.PlaceholderField(editable=False, null=True, slotname='search_results', to='cms.Placeholder')),
            ],
            options={
                'verbose_name_plural': 'Search results',
                'verbose_name': 'Search result',
            },
        ),
        migrations.CreateModel(
            name='SearchResultsTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('language_code', models.CharField(db_index=True, max_length=15)),
                ('master', models.ForeignKey(editable=False, null=True, to='searcher.SearchResults', related_name='translations')),
            ],
            options={
                'abstract': False,
                'db_table': 'searcher_searchresults_translation',
                'managed': True,
                'default_permissions': (),
                'db_tablespace': '',
            },
        ),
        migrations.AlterUniqueTogether(
            name='searchresultstranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
