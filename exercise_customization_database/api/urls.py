from django.conf.urls import include, url
from exercise_customization_database.api.views.workout_view import WorkoutView

urlpatterns = [
	url(r'^workouts/', WorkoutView.as_view()) 
]