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