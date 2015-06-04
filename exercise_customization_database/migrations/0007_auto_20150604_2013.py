# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_customization_database', '0006_auto_20150604_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='other_muscles',
            field=models.CharField(default=b'', max_length=175, null=True, blank=True),
        ),
    ]
