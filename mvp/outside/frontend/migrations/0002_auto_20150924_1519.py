# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='google_places_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='website',
            field=models.URLField(null=True, blank=True),
        ),
    ]
