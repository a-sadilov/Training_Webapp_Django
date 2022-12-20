from django.contrib import admin
from .models import  Person, Training, TrainingTask, Day, UserSettings, UserMeasurements


# Register your models here.

admin.site.register(Day)
admin.site.register(Training)
admin.site.register(TrainingTask)
admin.site.register(Person)
admin.site.register(UserSettings)
admin.site.register(UserMeasurements)