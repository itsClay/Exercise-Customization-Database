from django.core.management.base import BaseCommand
from exercise_customization_database.models import Exercise, Rating
import json, os

class Command(BaseCommand):

	def handle(self, *args, **options):

		with open('workout.json') as jsonfile:
			data = json.load(jsonfile)

		#Exercise Names	
		for exercise in data:
			name = exercise.keys()[0]

			# Exercise Properties we will save
			exerciseObject, created = Exercise.objects.update_or_create(
				name = name,
				equipment = exercise[name].get(u'Equipment', ''),
				force = exercise[name].get(u'Force',''),
				level = exercise[name].get(u'Level',''),
				main_muscle_worked = exercise[name].get(u'Main Muscle Worked',''),
				mechanics_type = exercise[name].get(u'Mechanics Type',''),
				other_muscles =	exercise[name].get(u'Other Muscles',''),
				exercise_type = exercise[name].get(u'Type',''),
				guide = ('').join(exercise[name].get(u'guide', '')),
				defaultRating = exercise[name].get(u'Your Rating', ' ')
			)
			exerciseObject.save()

