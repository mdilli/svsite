# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django_extensions.db.fields
import svfinance.utils
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0005_auto_20160323_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=48, help_text='Names should start with a letter and contain only letters, numbers and interpunction (like .,-_).')),
                ('code', models.CharField(default=None, max_length=48, blank=True, validators=[django.core.validators.RegexValidator('[A-Z]', 'Capital letters are not allowed.', inverse_match=True), django.core.validators.RegexValidator('__', 'Repeated underscores are not allowed.', inverse_match=True), django.core.validators.RegexValidator('^[a-z0-9_]+$', 'The value can only contain letters, numbers and underscores.'), django.core.validators.RegexValidator('^[a-z].*[a-z0-9]$', 'The value should start with a letter and end in a letter or number.'), django.core.validators.RegexValidator('[a-z0-9_]', 'Only letters, numbers and underscores are allowed'), django.core.validators.MinLengthValidator(2, 'The minimum length is 2.'), django.core.validators.MaxLengthValidator(48, 'The maximum length is 48.')], help_text='will be automatically determined from the name if empty')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Expenses'), (2, 'Asset'), (3, 'Liability'), (4, 'Debtor/creditor')])),
                ('order', models.PositiveSmallIntegerField(default=0, help_text='This determined in which order the accounts are displayed in reports.')),
                ('is_category', models.BooleanField(default=False, help_text='Category accounts are just for organization. You can add other accounts as children, but cannot add. Only same-type accounts can be children.')),
                ('parent', models.ForeignKey(null=True, blank=True, to='svfinance.Account', related_name='children')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(unique=True, validators=[django.core.validators.RegexValidator('[A-Z]', 'Capital letters are not allowed.', inverse_match=True), django.core.validators.RegexValidator('__', 'Repeated underscores are not allowed.', inverse_match=True), django.core.validators.RegexValidator('^[a-z0-9_]+$', 'The value can only contain letters, numbers and underscores.'), django.core.validators.RegexValidator('^[a-z].*[a-z0-9]$', 'The value should start with a letter and end in a letter or number.'), django.core.validators.RegexValidator('[a-z0-9_]', 'Only letters, numbers and underscores are allowed'), django.core.validators.MinLengthValidator(2, 'The minimum length is 2.'), django.core.validators.MaxLengthValidator(48, 'The maximum length is 48.')], max_length=16)),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, blank=True, populate_from='name')),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PeriodAccess',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('can_edit', models.BooleanField(default=False)),
                ('period', models.ForeignKey(to='svfinance.Period', related_name='accesses')),
                ('team', models.ForeignKey(to='member.Team', related_name='periods_accesses')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('account', models.ForeignKey(null=True, blank=True, to='svfinance.Account', related_name='lines')),
                ('transaction', models.ForeignKey(to='svfinance.Transaction', related_name='lines')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionValidation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
            field=models.OneToOneField(null=True, blank=True, to='svfinance.Account', help_text='Which account corresponds to this one in the last booking period, if any?', related_name='next_period_account'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL, help_text='If this is a debtor/creditor account, set the user here.', related_name='finance_accounts'),
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together=set([('period', 'code'), ('period', 'name')]),
        ),
    ]
