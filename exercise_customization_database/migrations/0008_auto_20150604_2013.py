# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_customization_database', '0007_auto_20150604_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exercise_type',
            field=models.CharField(default=b'', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='force',
            field=models.CharField(default=b'', max_length=100, null=True, blank=True),
        ),
    ]
