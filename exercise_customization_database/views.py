from django.shortcuts import render

# Create your views here.
def workouts(request):
	return render(request, 'exercise_customization_database/workouts.html')