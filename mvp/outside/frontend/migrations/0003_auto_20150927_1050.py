# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('frontend', '0002_auto_20150924_1519'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClosingEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proof', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('lead', models.ForeignKey(to='frontend.Lead')),
            ],
        ),
        migrations.AddField(
            model_name='seller',
            name='logo',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='closingevent',
            name='seller',
            field=models.ForeignKey(to='frontend.Seller'),
        ),
        migrations.AddField(
            model_name='closingevent',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='closingevent',
            unique_together=set([('user', 'lead', 'seller')]),
        ),
    ]
