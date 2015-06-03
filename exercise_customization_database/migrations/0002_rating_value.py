# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_customization_database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='value',
            field=models.SmallIntegerField(default=b'10'),
        ),
    ]
