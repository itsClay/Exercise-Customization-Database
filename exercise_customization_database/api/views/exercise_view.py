from rest_framework.generics import ListCreateAPIView
from exercise_customization_database.api.serializers.workout_serializer import ExerciseSerializer 
from exercise_customization_database.models import Exercise

class ExerciseView(ListCreateAPIView): #this might need to be changed to allow a create or delete as well. Can't access docs right now
	serializer_class = ExerciseSerializer

	def get_queryset(self):
		return Exercise.objects.all()