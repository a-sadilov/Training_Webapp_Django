from rest_framework import  serializers
from .models import  UserMeasurements, UserSettings, Person, TrainingTask
from calendarapp.models import Event

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = "__all__"


class PersonSerializer(serializers.ModelSerializer):
    user_settings = UserSettingsSerializer()
    class Meta:
        model = Person
        fields = "__all__"

class UserMeasurementsSerializer(serializers.ModelSerializer):
    #id = serializers.CharField()
    class Meta:
        model = UserMeasurements
        fields = "__all__"


class TrainingTaskSerializer(serializers.ModelSerializer):
    task_settings = UserSettingsSerializer()
    class Meta:
        model = TrainingTask
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    tasks = TrainingTaskSerializer(many=True)
    class Meta:
        model = Event
        fields = "__all__"
    
