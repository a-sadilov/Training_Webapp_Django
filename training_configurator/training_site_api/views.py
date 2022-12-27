from django.shortcuts import render
from rest_framework import viewsets

from .models import  Person, TrainingTask, UserSettings, UserMeasurements
from calendarapp.models import Event
from .serializers import *
#from django_filters import FilterSet,CharFilter
from django.contrib.auth.decorators import login_required
from rest_framework import filters, status
from rest_framework.decorators import api_view, permission_classes
#from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .crud_mixin import *
from rest_framework import permissions

"""# Create your views here.
class EventSetFilter(FilterSet):
    name__icontains = CharFilter(field_name="name",lookup_expr="icontains")
    class Meta:
        model = Event
        fields = "__all__"
        exclude = []

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    model = Event
    serializer_class = EventSerializer
    filterset_class = EventSetFilter
# get, post, delete, update
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
# get, delete, update
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
# get, post, delete, update

class UserSettingsViewSet(viewsets.ModelViewSet):
    queryset = UserSettings.objects.all()
    serializer_class = UserSettingsSerializer
# get, update

class UserMeasurementsViewSet(viewsets.ModelViewSet):
    queryset = UserMeasurements.objects.all()
    serializer_class = UserMeasurementsSerializer
# get, post, delete, update"""


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description')
    permission_classes = [permissions.DjangoModelPermissions]
    http_method_names = ['get', 'post', 'head', 'delete', 'update']

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    http_method_names = ['get', 'head', 'delete', 'update']

class UserSettingsViewSet(viewsets.ModelViewSet):
    queryset = UserSettings.objects.all()
    serializer_class = UserSettingsSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    http_method_names = ['get', 'head', 'update']

class TrainingTaskViewSet(viewsets.ModelViewSet):
    queryset = TrainingTask.objects.all()
    serializer_class = TrainingTaskSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [permissions.DjangoModelPermissions]
    search_fields = ('name', 'task_type', 'musclegroup_type')
    http_method_names = ['get', 'post', 'head', 'delete', 'update']


class UserMeasurementsViewSet(viewsets.ModelViewSet):
    queryset = UserMeasurements.objects.all()
    serializer_class = UserMeasurementsSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [permissions.DjangoModelPermissions]
    search_fields = ('name')
    http_method_names = ['get', 'post', 'head', 'delete', 'update']

'''@login_required
def index(request):
    return render(request, 'base.html', {})


@login_required
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Event List': '/event-list/',
        'Event Detail': '/event-detail/<str:pk>/',
        'Event Create': '/event-create/',
        'Event Update': '/event-update/<str:pk>/',
        'Event Delete': '/event-delete/<str:pk>/',

        'Task List': '/task-list/',
        'Task Detail': '/task-detail/<str:pk>/',
        'Task Create': '/task-create/',
        'Task Update': '/task-update/<str:pk>/',
        'Task Delete': '/task-delete/<str:pk>/',

        'Person Detail ': '/person-detail/<str:pk>/',
        'Person Update': '/person-update/<str:pk>/',
        'Person Delete': '/person-delete/<str:pk>/',

        'Measurements List': '/measurements-list/',
        'Measurements Detail': '/measurements-detail/<str:pk>/',
        'Measurements Create': '/measurements-create/',
        'Measurements Update': '/measurements-update/<str:pk>/',
        'Measurements Delete': '/measurements-delete/<str:pk>/',

        'Settings Detail': '/settings-detail/<str:pk>/',
        'Settings Update': '/settings-update/<str:pk>/',
    }
    return Response(api_urls)


class EventApiView(List_Mixin, Update_Mixin, Delete_Mixin, Get_Mixin, Post_Mixin):
    model_type = Event
    serializer = EventSerializer

    @login_required
    def List(self, request):
        return super(EventApiView, self).List(request)
    
    @login_required
    def Update(self, request, pk):
        return super(EventApiView, self).Update(request, pk)
    
    @login_required
    def Delete(self, request, pk):
        return super(EventApiView, self).Delete(request, pk)
    
    @login_required
    def Detail(self, request, pk):
        return super(EventApiView, self).Detail(request, pk)
    
    @login_required
    def Create(self, request):
        return super(EventApiView, self).Create(request)

class MeasurementsApiView(List_Mixin, Update_Mixin, Delete_Mixin, Get_Mixin, Post_Mixin):
    model_type = UserMeasurements
    serializer = UserMeasurementsSerializer

    @login_required
    def List(self, request):
        return super(MeasurementsApiView, self).List(request)
    
    @login_required
    def Update(self, request, pk):
        return super(MeasurementsApiView, self).Update(request, pk)
    
    @login_required
    def Delete(self, request, pk):
        return super(MeasurementsApiView, self).Delete(request, pk)
    
    @login_required
    def Detail(self, request, pk):
        return super(MeasurementsApiView, self).Detail(request, pk)
    
    @login_required
    def Create(self, request):
        return super(MeasurementsApiView, self).Create(request)


class PersonApiView(Update_Mixin, Delete_Mixin, Get_Mixin):
    model_type = Person
    serializer = PersonSerializer

    
    @login_required
    def Update(self, request, pk):
        return super(PersonApiView, self).Update(request, pk)
    
    @login_required
    def Delete(self, request, pk):
        return super(PersonApiView, self).Delete(request, pk)
    
    @login_required
    def Detail(self, request, pk):
        return super(PersonApiView, self).Detail(request, pk)
    



class TaskApiView(List_Mixin, Update_Mixin, Delete_Mixin, Get_Mixin, Post_Mixin):
    model_type = TrainingTask
    serializer = TrainingTaskSerializer

    @login_required
    def List(self, request):
        return super(TaskApiView, self).List(request)
    
    @login_required
    def Update(self, request, pk):
        return super(TaskApiView, self).Update(request, pk)
    
    @login_required
    def Delete(self, request, pk):
        return super(TaskApiView, self).Delete(request, pk)
    
    @login_required
    def Detail(self, request, pk):
        return super(TaskApiView, self).Detail(request, pk)
    
    @login_required
    def Create(self, request):
        return super(TaskApiView, self).Create(request)


class SettingsApiView(Update_Mixin, Get_Mixin):
    model_type = UserSettings
    serializer = UserSettingsSerializer
    
    @login_required
    def Detail(self, request, pk):
        return super(PersonApiView, self).Detail(request, pk)
    
    @login_required
    def Update(self, request, pk):
        return super(PersonApiView, self).Update(request, pk)'''