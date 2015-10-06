# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(db_index=True)),
                ('address', models.TextField(db_index=True)),
                ('phone', models.TextField(null=True, blank=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('contact_name', models.TextField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('closed', models.BooleanField(default=False)),
                ('lost', models.BooleanField(default=False)),
                ('repeat_at', models.DateTimeField(db_index=True, null=True, blank=True)),
                ('last_visited_at', models.DateTimeField(db_index=True, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('lng', models.FloatField(default=0.0)),
                ('lat', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(db_index=True)),
                ('description', models.TextField(db_index=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('owned_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lead',
            name='last_visited_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='frontend.Seller', null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='owned_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=None, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
