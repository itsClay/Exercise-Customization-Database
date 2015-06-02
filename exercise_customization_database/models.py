from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.contrib.auth.models import user

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)

     def __unicode__(self):
        return self.UserProfile

class Workout(models.Model):
	name = models.CharField(max_length=75)

	def __unicode__(self):
        return self.Workout

class Exercise(models.Model):
	name = models.CharField(max_length=75, blank=True, default='')
	equipment = models.CharField(max_length=75, blank=True, default='', null=True)
	force = models.CharField(max_length=20, blank=True, default='', null=True)
	level = models.CharField(max_length=75, blank=True, default='', null=True)
	main_muscle_worked = models.CharField(max_length=75, blank=True, default='', null=True)
	mechanics_type = models.CharField(max_length=75, blank=True, default='', null=True)
	other_muscles = models.CharField(max_length=75, blank=True, default='', null=True)
	exercise_type = models.CharField(max_length=20, null=True)
	rating = models.SmallIntegerField(null=True)

	def __unicode__(self):
	   return self.Exercise

class Rating(models.Model):
	rating = models.OneToManyField(null=True)

	def __unicode__(self):
	   return self.Rating
