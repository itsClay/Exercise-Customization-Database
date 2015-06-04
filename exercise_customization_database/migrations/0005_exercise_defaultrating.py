# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_customization_database', '0004_auto_20150604_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='defaultRating',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
