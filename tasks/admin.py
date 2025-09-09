from django.contrib import admin
from .models import Task, Tag

# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "priority", "is_archived", "created_at")
    list_filter = ("status", "priority", "is_archived", "created_at")
    search_fields = ("title", "description")
    filter_horizontal = ("assigned_to", "tags")
