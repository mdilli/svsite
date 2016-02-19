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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('placeholder', cms.models.fields.PlaceholderField(to='cms.Placeholder', slotname='search_results', null=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SearchResultsTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(to='base.SearchResults', related_name='translations', null=True, editable=False)),
            ],
            options={
                'abstract': False,
                'db_tablespace': '',
                'db_table': 'base_searchresults_translation',
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='searchresultstranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
