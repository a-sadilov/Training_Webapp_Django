from django.urls import include, path
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from rest_framework import routers
from training_site_api.views import EventViewSet, TrainingTaskViewSet, PersonViewSet, UserSettingsViewSet, UserMeasurementsViewSet
#from .views import apiOverview, PersonApiView, EventApiView, MeasurementsApiView, SettingsApiView, TaskApiView

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'event', EventViewSet)
router.register(r'task', TrainingTaskViewSet)
router.register(r'person', PersonViewSet)
router.register(r'settings', UserSettingsViewSet)
router.register(r'measurements', UserMeasurementsViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    

    
]
'''

    path('api/', apiOverview, name="api-overview"),
    path('person-detail/<str:pk>/', PersonApiView.Detail, name="person-detail"),
    path('person-update/<str:pk>/', PersonApiView.Update, name="person-update"),
    path('person-delete/<str:pk>/', PersonApiView.Delete, name="person-delete"),

    path('event-list', EventApiView.List, name="event-list"),
    path('event-detail/<str:pk>/', EventApiView.Detail, name="event-detail"),
    path('event-create/', EventApiView.Create, name="event-create"),
    path('event-update/<str:pk>/', EventApiView.Update, name="event-update"),
    path('event-delete/<str:pk>/', EventApiView.Delete, name="event-delete"),

    path('task-list', TaskApiView.List, name="task-list"),
    path('task-detail/<str:pk>/', TaskApiView.Detail, name="task-detail"),
    path('task-create/', TaskApiView.Create, name="task-create"),
    path('task-update/<str:pk>/', TaskApiView.Update, name="task-update"),
    path('task-delete/<str:pk>/', TaskApiView.Delete, name="task-delete"),

    path('measurements-list', MeasurementsApiView.List, name="measurements-list"),
    path('measurements-detail/<str:pk>/', MeasurementsApiView.Detail, name="measurements-detail"),
    path('measurements-create/', MeasurementsApiView.Create, name="measurements-create"),
    path('measurements-update/<str:pk>/', MeasurementsApiView.Update, name="measurements-update"),
    path('measurements-delete/<str:pk>/', MeasurementsApiView.Delete, name="measurements-delete"),

    path('settings-detail/<str:pk>/', SettingsApiView.Detail, name="settings-detail"),
    path('settings-update/<str:pk>/', SettingsApiView.Update, name="settings-update"),'''