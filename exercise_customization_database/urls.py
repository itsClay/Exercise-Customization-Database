from django.conf.urls import url
from exercise_customization_database import views

urlpatterns = [
	url(r'', views.workouts , name='workouts')
]