from django.contrib import admin
from models import UserProfile, Workout, Exercise, Rating

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Rating)

