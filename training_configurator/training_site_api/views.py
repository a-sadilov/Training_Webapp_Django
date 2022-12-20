from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .models import  Person, Training, TrainingTask, Day, UserSettings, UserMeasurements
from .serializers import *
from django_filters import FilterSet,CharFilter

# Create your views here.
class TrainingSetFilter(FilterSet):
    name__icontains = CharFilter(field_name="name",lookup_expr="icontains")
    class Meta:
        model = Training
        fields = "__all__"
        exclude = []

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    model = Training
    serializer_class = TrainingSerializer
    filterset_class = TrainingSetFilter

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class TrainingTaskSetFilter(FilterSet):
    name__icontains = CharFilter(field_name="name",lookup_expr="icontains")
    class Meta:
        model = TrainingTask
        fields = "__all__"
        exclude = []

class TrainingTaskViewSet(viewsets.ModelViewSet):
    queryset = TrainingTask.objects.all()
    model = TrainingTask
    serializer_class = TrainingTaskSerializer
    filterset_class = TrainingTaskSetFilter

class UserSettingsViewSet(viewsets.ModelViewSet):
    queryset = UserSettings.objects.all()
    serializer_class = UserSettingsSerializer

class UserMeasurementsViewSet(viewsets.ModelViewSet):
    queryset = UserMeasurements.objects.all()
    serializer_class = UserMeasurementsSerializer

class DaySetFilter(FilterSet):
    date__icontains = CharFilter(field_name="date",lookup_expr="icontains")
    class Meta:
        model = Day
        fields = "__all__"
        exclude = []

class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    model = Day
    serializer_class = DaySerializer
    filterset_class = DaySetFilter