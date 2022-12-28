from .models import  Person, TrainingTask, UserSettings, UserMeasurements
from calendarapp.models import Event
from .serializers import *
from rest_framework import filters, viewsets
from rest_framework import permissions


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description')
    permission_classes = [permissions.DjangoModelPermissions]
    http_method_names = ['get', 'post', 'head', 'delete', 'update']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    http_method_names = ['get', 'head', 'delete', 'update']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)

class UserSettingsViewSet(viewsets.ModelViewSet):
    queryset = UserSettings.objects.all()
    serializer_class = UserSettingsSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    http_method_names = ['get', 'head', 'update']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)

class TrainingTaskViewSet(viewsets.ModelViewSet):
    queryset = TrainingTask.objects.all()
    serializer_class = TrainingTaskSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [permissions.DjangoModelPermissions]
    search_fields = ('name', 'task_type', 'musclegroup_type')
    http_method_names = ['get', 'post', 'head', 'delete', 'update']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)


class UserMeasurementsViewSet(viewsets.ModelViewSet):
    queryset = UserMeasurements.objects.all()
    serializer_class = UserMeasurementsSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [permissions.DjangoModelPermissions]
    search_fields = ('name')
    http_method_names = ['get', 'post', 'head', 'delete', 'update']
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user = self.request.user)

