from django.contrib import admin
from .models import  Person, TrainingTask, UserSettings, UserMeasurements


# Register your models here.

admin.site.register(TrainingTask)
admin.site.register(Person)
admin.site.register(UserSettings)
admin.site.register(UserMeasurements)