# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators
import forum.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(max_length=200, null=True, blank=True)),
                ('avatar', models.CharField(max_length=200, null=True, blank=True)),
                ('signature', models.CharField(max_length=500, null=True, blank=True)),
                ('location', models.CharField(max_length=200, null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('company', models.CharField(max_length=200, null=True, blank=True)),
                ('role', models.IntegerField(null=True, blank=True)),
                ('balance', models.IntegerField(null=True, blank=True)),
                ('reputation', models.IntegerField(null=True, blank=True)),
                ('self_intro', models.CharField(max_length=500, null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('twitter', models.CharField(max_length=200, null=True, blank=True)),
                ('github', models.CharField(max_length=200, null=True, blank=True)),
                ('douban', models.CharField(max_length=200, null=True, blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
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
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('involved_type', models.IntegerField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('slug', models.SlugField(max_length=200, null=True, blank=True)),
                ('thumb', models.CharField(max_length=200, null=True, blank=True)),
                ('introduction', models.CharField(max_length=500, null=True, blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('topic_count', models.IntegerField(null=True, blank=True)),
                ('custom_style', forum.models.NormalTextField(null=True, blank=True)),
                ('limit_reputation', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', forum.models.NormalTextField(null=True, blank=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('involved_type', models.IntegerField(null=True, blank=True)),
                ('occurrence_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', forum.models.NormalTextField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('up_vote', models.IntegerField(null=True, blank=True)),
                ('down_vote', models.IntegerField(null=True, blank=True)),
                ('last_touched', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(related_name='reply_author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('slug', models.SlugField(max_length=200, null=True, blank=True)),
                ('content', forum.models.NormalTextField(null=True, blank=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('hits', models.IntegerField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('reply_count', models.IntegerField(null=True, blank=True)),
                ('last_replied_time', models.DateTimeField(null=True, blank=True)),
                ('up_vote', models.IntegerField(null=True, blank=True)),
                ('down_vote', models.IntegerField(null=True, blank=True)),
                ('last_touched', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(related_name='topic_author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('last_replied_by', models.ForeignKey(related_name='topic_last', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('node', models.ForeignKey(blank=True, to='forum.Node', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(null=True, blank=True)),
                ('reward', models.IntegerField(null=True, blank=True)),
                ('current_balance', models.IntegerField(null=True, blank=True)),
                ('occurrence_time', models.DateTimeField(null=True, blank=True)),
                ('involved_reply', models.ForeignKey(related_name='trans_reply', blank=True, to='forum.Reply', null=True)),
                ('involved_topic', models.ForeignKey(related_name='trans_topic', blank=True, to='forum.Topic', null=True)),
                ('involved_user', models.ForeignKey(related_name='trans_involved', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(related_name='trans_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('involved_type', models.IntegerField(null=True, blank=True)),
                ('occurrence_time', models.DateTimeField(null=True, blank=True)),
                ('involved_reply', models.ForeignKey(related_name='vote_reply', blank=True, to='forum.Reply', null=True)),
                ('involved_topic', models.ForeignKey(related_name='vote_topic', blank=True, to='forum.Topic', null=True)),
                ('involved_user', models.ForeignKey(related_name='vote_user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('trigger_user', models.ForeignKey(related_name='vote_trigger', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='reply',
            name='topic',
            field=models.ForeignKey(blank=True, to='forum.Topic', null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='involved_reply',
            field=models.ForeignKey(related_name='notify_reply', blank=True, to='forum.Reply', null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='involved_topic',
            field=models.ForeignKey(related_name='notify_topic', blank=True, to='forum.Topic', null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='involved_user',
            field=models.ForeignKey(related_name='notify_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='trigger_user',
            field=models.ForeignKey(related_name='notify_trigger', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='plane',
            field=models.ForeignKey(blank=True, to='forum.Plane', null=True),
        ),
        migrations.AddField(
            model_name='favorite',
            name='involved_reply',
            field=models.ForeignKey(related_name='fav_reply', blank=True, to='forum.Reply', null=True),
        ),
        migrations.AddField(
            model_name='favorite',
            name='involved_topic',
            field=models.ForeignKey(related_name='fav_topic', blank=True, to='forum.Topic', null=True),
        ),
        migrations.AddField(
            model_name='favorite',
            name='owner_user',
            field=models.ForeignKey(related_name='fav_user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
