# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_auto_20150927_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='reward',
            field=models.FloatField(default=0.0),
        ),
    ]
