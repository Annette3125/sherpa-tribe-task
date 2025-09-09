from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Task, Comment, Team
from .serializers import TaskSerializer, CommentSerializer, TeamSerializer
# Create your views here.


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all().select_related("created_by", "parent_task").prefetch_related("assigned_to", "tags", "comments")
    serializer_class = TaskSerializer

    filterset_fields = ["status", "priority", "is_archived"]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "priority", "due_date"]
    ordering = ["-created_at"]

    # nested endpoint /api/tasks/{id}/comments/
    @action(detail=True, methods=["get", "post"], url_path="comments")
    def comments(self, request, pk=None):
        task = self.get_object()
        if request.method.lower() == "get":
            qs = task.comments.select_related("author").all()
            return Response(CommentSerializer(qs, many=True).data)

        data = request.data.copy()
        data["task"] = task.pk
        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().select_related("task", "author")
    serializer_class = CommentSerializer

    filterset_fields = ["task", "author"]
    search_fields = ["body"]
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all().prefetch_related("members")
    serializer_class = TeamSerializer

    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = ["name", "created_at"]
    ordering = ["name"]
