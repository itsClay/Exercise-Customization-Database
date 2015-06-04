# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_customization_database', '0003_auto_20150602_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exercise_type',
            field=models.CharField(default=b'', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='guide',
            field=models.TextField(default=b'', null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(default=b'', unique=True, max_length=75, blank=True),
        ),
    ]
