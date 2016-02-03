# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
import django.contrib.auth.models
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], verbose_name='username', error_messages={'unique': 'A user with that username already exists.'}, unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, blank=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from='username', editable=False, unique=True, blank=True)),
                ('birthday', models.DateField(blank=True, default=None, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('group_ptr', models.OneToOneField(to='auth.Group', primary_key=True, auto_created=True, serialize=False, parent_link=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(populate_from='name', editable=False, help_text='This value is used as identifier in places like urls.', blank=True, unique=True)),
                ('listed', models.BooleanField(default=False)),
                ('description', models.TextField(default='', blank=True)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        ),
        migrations.AddField(
            model_name='member',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.'),
        ),
    ]
