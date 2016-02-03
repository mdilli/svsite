# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import django.utils.timezone
from django.conf import settings
import ctrl.models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], error_messages={'unique': 'A user with that username already exists.'})),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('slug', django_extensions.db.fields.AutoSlugField(editable=False, blank=True, populate_from='username', unique=True)),
                ('birthday', models.DateField(null=True, blank=True, default=None)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', ctrl.models.UserPermissionManager()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('group_ptr', models.OneToOneField(parent_link=True, primary_key=True, to='auth.Group', auto_created=True, serialize=False)),
            ],
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='TeamRole',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('member', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(to='member.Team')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='groups',
            field=models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', to='member.Team', related_query_name='user', blank=True, verbose_name='groups', through='member.TeamRole'),
        ),
        migrations.AddField(
            model_name='member',
            name='user_permissions',
            field=models.ManyToManyField(help_text='Specific permissions for this user.', related_name='user_set', to='auth.Permission', related_query_name='user', blank=True, verbose_name='user permissions'),
        ),
    ]
