from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer
# Create your views here.


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all().select_related("created_by", "parent_task").prefetch_related("assigned_to", "tags")
    serializer_class = TaskSerializer

    filterset_fields = ["status", "priority", "is_archived"]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "priority", "due_date"]
    ordering = ["-created_at"]