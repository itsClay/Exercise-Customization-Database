# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=75, blank=True)),
                ('equipment', models.CharField(default=b'', max_length=75, null=True, blank=True)),
                ('force', models.CharField(default=b'', max_length=20, null=True, blank=True)),
                ('level', models.CharField(default=b'', max_length=75, null=True, blank=True)),
                ('main_muscle_worked', models.CharField(default=b'', max_length=75, null=True, blank=True)),
                ('mechanics_type', models.CharField(default=b'', max_length=75, null=True, blank=True)),
                ('other_muscles', models.CharField(default=b'', max_length=75, null=True, blank=True)),
                ('exercise_type', models.CharField(max_length=20, null=True)),
                ('guide', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.ForeignKey(to='exercise_customization_database.Exercise', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('workout_name', models.CharField(max_length=75)),
                ('exercises', models.ManyToManyField(to='exercise_customization_database.Exercise')),
                ('user', models.ForeignKey(to='exercise_customization_database.UserProfile')),
            ],
        ),
    ]
