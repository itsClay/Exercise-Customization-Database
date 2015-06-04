from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return '{}'.format(self.user.username)

class Workout(models.Model):
	workout_name = models.CharField(max_length=75)
	user = models.ForeignKey('UserProfile')
	exercises = models.ManyToManyField('Exercise')

	def __unicode__(self):
		return '{}'.format(self.workout_name)

class Exercise (models.Model):
	name = models.CharField(max_length=100, blank=True, default='', unique=True)
	equipment = models.CharField(max_length=75, blank=True, default='', null=True)
	force = models.CharField(max_length=100, blank=True, default='', null=True)
	level = models.CharField(max_length=75, blank=True, default='', null=True)
	main_muscle_worked = models.CharField(max_length=75, blank=True, default='', null=True)
	mechanics_type = models.CharField(max_length=75, blank=True, default='', null=True)
	other_muscles = models.CharField(max_length=175, blank=True, default='', null=True)
	exercise_type = models.CharField(max_length=100, default='', null=True)
	guide = models.TextField(default='', null=True)
	defaultRating = models.CharField(max_length=3, null=True)

	def __unicode__(self):
	   return '{}'.format(self.name)

class Rating(models.Model):
	rating = models.SmallIntegerField(default='10')
	exercise = models.ForeignKey('Exercise', null=True)

	def __str__(self):
	   return '{}'.format(self.rating)
