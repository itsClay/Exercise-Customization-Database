from django.conf.urls import include, url
from exercise_customization_database.api.views.exercise_view import ExerciseView

urlpatterns = [
	url(r'^exercises/', ExerciseView.as_view()) 
]