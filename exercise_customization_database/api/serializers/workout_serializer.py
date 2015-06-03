from rest_framework import serializers
from exercise_customization_database.models import Exercise 

class WorkoutSerializer(serializers.ModelSerializer):
	class Meta:
		model = Exercise