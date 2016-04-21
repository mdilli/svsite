# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
import django.utils.timezone
from django.conf import settings
import django.core.validators
import svfinance.utils


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_auto_20160323_2221'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=48, help_text='Names should start with a letter and contain only letters, numbers and interpunction (like .,-_).')),
                ('code', models.CharField(validators=[django.core.validators.RegexValidator('[A-Z]', 'Capital letters are not allowed.', inverse_match=True), django.core.validators.RegexValidator('__', 'Repeated underscores are not allowed.', inverse_match=True), django.core.validators.RegexValidator('^[a-z0-9_]+$', 'The value can only contain letters, numbers and underscores.'), django.core.validators.RegexValidator('^[a-z].*[a-z0-9]$', 'The value should start with a letter and end in a letter or number.'), django.core.validators.RegexValidator('[a-z0-9_]', 'Only letters, numbers and underscores are allowed'), django.core.validators.MinLengthValidator(2, 'The minimum length is 2.'), django.core.validators.MaxLengthValidator(48, 'The maximum length is 48.')], unique=True, default=None, max_length=48, blank=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Expenses'), (2, 'Expenses'), (3, 'Expenses'), (4, 'Debtor/creditor'), (5, 'Category')])),
                ('order', models.PositiveSmallIntegerField(help_text='This determined in which order the accounts are displayed in reports.')),
                ('parent', models.ForeignKey(related_name='children', to='svfinance.Account', null=True, blank=True)),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator('[A-Z]', 'Capital letters are not allowed.', inverse_match=True), django.core.validators.RegexValidator('__', 'Repeated underscores are not allowed.', inverse_match=True), django.core.validators.RegexValidator('^[a-z0-9_]+$', 'The value can only contain letters, numbers and underscores.'), django.core.validators.RegexValidator('^[a-z].*[a-z0-9]$', 'The value should start with a letter and end in a letter or number.'), django.core.validators.RegexValidator('[a-z0-9_]', 'Only letters, numbers and underscores are allowed'), django.core.validators.MinLengthValidator(2, 'The minimum length is 2.'), django.core.validators.MaxLengthValidator(48, 'The maximum length is 48.')])),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from='name', editable=False, blank=True)),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PeriodAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('can_edit', models.BooleanField(default=False)),
                ('period', models.ForeignKey(to='svfinance.Period', related_name='accesses')),
                ('team', models.ForeignKey(to='member.Team', related_name='periods_accesses')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('message', models.TextField(validators=[django.core.validators.MinLengthValidator(4)])),
                ('date', models.DateField(default=svfinance.utils.today)),
                ('created_on', models.DateTimeField(default=None)),
                ('edited_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
                ('edited_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionLine',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('amount', models.DecimalField(max_digits=12, decimal_places=2)),
                ('account', models.ForeignKey(related_name='transaction_lines', to='svfinance.Account', null=True, blank=True)),
                ('transaction', models.ForeignKey(to='svfinance.Transaction', related_name='lines')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransactionValidation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('auditor', models.ForeignKey(to='member.Team', related_name='+')),
                ('transaction', models.ForeignKey(to='svfinance.Transaction', related_name='validations')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='period',
            field=models.ForeignKey(to='svfinance.Period', related_name='accounts'),
        ),
        migrations.AddField(
            model_name='account',
            name='prev_period_account',
            field=models.OneToOneField(to='svfinance.Account', null=True, related_name='next_period_account', help_text='Which account corresponds to this one in the last booking period, if any?', blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(null=True, related_name='finance_accounts', to=settings.AUTH_USER_MODEL),
        ),
    ]
