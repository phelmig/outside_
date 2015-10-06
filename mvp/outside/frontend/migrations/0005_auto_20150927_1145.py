# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_seller_reward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='last_visited_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='owned_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=None, to='frontend.Seller', null=True),
        ),
    ]
