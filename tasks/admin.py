from django.contrib import admin
from .models import Task, Tag, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ("author", "body", "created_at")
    readonly_fields = ("created_at",)

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
    inlines = [CommentInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "task", "author", "created_at")
    list_filter = ("created_at",)
    search_fields = ("body",)