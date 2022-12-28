
from django.urls import include, path
from django.contrib import admin
from django.urls import path
from .views import DashboardView

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("", include("calendarapp.urls")),
    path("accounts/", include("accounts.urls")),
    path("", include("training_site_api.urls")),
    path("admin/", admin.site.urls),
]
