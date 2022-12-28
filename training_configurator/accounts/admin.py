from django.contrib import admin
from accounts import models


@admin.register(models.User)
class EventAdmin(admin.ModelAdmin):
    model = models.User
    list_display = [
        "id",
        "email",
        "is_staff",
        "is_active",
        "date_joined",
        "last_updated",
    ]
    list_filter = ["is_active", "is_staff"]
    search_fields = ["email"]