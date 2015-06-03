# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_customization_database', '0002_rating_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='value',
        ),
        migrations.AddField(
            model_name='rating',
            name='exercise',
            field=models.ForeignKey(to='exercise_customization_database.Exercise', null=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.SmallIntegerField(default=b'10'),
        ),
    ]
