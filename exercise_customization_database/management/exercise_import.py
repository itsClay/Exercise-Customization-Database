from django.core.management.base import BaseCommand
from exercise_customization_database.models import Exercise, Rating
import json, os

class Command(BaseCommand):

	def handle(self, *args, **options):
		with open('workout.json') as jsonfile:
			workout_json = json.load(jsonfile)

		#Exercise Names	
		for exercise in workout_json
			try:
				exerciseObject = Exercise.object.get(name = exercise.keys()[0])

			except exerciseObject.DoesNotExist:
				exerciseObject = Exercise(
					name = exercise[exercise.keys()[0]],
					equipment = exercise[exercise.keys()[0]][u'Equipment'].get('Equipment',''),
					force = exercise[exercise.keys()[0]][u'Force'].get('Force',''),
					level = exercise[exercise.keys()[0]][u'Level'].get('Level',''),
					main_muscle_worked = exercise[exercise.keys()[0]][u'Main Muscle Worked'].get('Main Muscle Worked',''),
					mechanics_type = exercise[exercise.keys()[0]][ u'Mechanics Type'].get('Mechanics Type',''),
					other_muscles =	exercise[exercise.keys()[0]][u'Other Muscles'].get('Other Muscles',''),
					exercise_type = exercise[exercise.keys()[0]][u'Type'].get('Type',''),
					guide = ('').join(exercise[exercise.keys()[0]][u'guide']),
					rating = exercise[exercise.keys()[0]][u'Your Rating'].get('Your Rating','')
				)
				exerciseObject.save()
			#If the Dict already exists in the db, this will overwrite the data values	
			else:
				exerciseObject.name = exercise[exercise.keys()[0]]
				exerciseObject.equipment = exercise[exercise.keys()[0]][u'Equipment'].get('Equipment','')
				exerciseObject.force = exercise[exercise.keys()[0]][u'Force'].get('Force','')
				exerciseObject.level = exercise[exercise.keys()[0]][u'Level'].get('Level','')
				exerciseObject.main_muscle_worked = exercise[exercise.keys()[0]][u'Main Muscle Worked'].get('Main Muscle Worked','')
				exerciseObject.mechanics_type = exercise[exercise.keys()[0]][ u'Mechanics Type'].get('Mechanics Type','')
				exerciseObject.other_muscles = exercise[exercise.keys()[0]][u'Other Muscles'].get('Other Muscles','')
				exerciseObject.exercise_type = exercise[exercise.keys()[0]][u'Type'].get('Type','')
				exerciseObject.guide = ('').join(exercise[exercise.keys()[0]][u'guide'])
				exerciseObject.rating = exercise[exercise.keys()[0]][u'Your Rating'].get('Your Rating','')
				exerciseObject.save()
				print("Else: ", exerciseObject)







"""
from django.core.management.base import BaseCommand
from StateData.models import EnergyProduction
from django.templatetags.static import static
import json
import os

class Command(BaseCommand):

   def handle(self, *args, **options):

       url = 'energyProduction.json'

       with open(url) as data_file:
           data = json.load(data_file)

       for record in data:
           try:
               stateRecord = EnergyProduction.objects.get(state=record[u'state'])
           except stateRecord.DoesNotExist:
               stateRecord = EnergyProduction(
                   state=record[u'state'],
                   coal=record[u'coal'],
                   gas=record[u'gas'],
                   oil=record[u'oil'],
                   nuclear=record[u'nuclear'],
                   biofuels=record[u'biofuels'],
                   othRenews=record[u'coal']
                   )
               stateRecord.save()
               print("Except:", stateRecord)
           else:
               stateRecord.coal=record[u'coal']
               stateRecord.gas=record[u'gas']
               stateRecord.oil=record[u'oil']
               stateRecord.nuclear=record[u'nuclear']
               stateRecord.biofuels=record[u'biofuels']
               stateRecord.othRenews=record[u'coal']
               stateRecord.save()
               print("Else: ", stateRecord)
"""