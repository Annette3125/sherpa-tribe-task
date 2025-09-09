from rest_framework import serializers
from .models import Task, Tag, Comment, Team

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "task", "author", "body", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class TaskSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)

    class Meta:
        model = Task
        fields = [
            "id","title","description",
            "status","priority",
            "due_date","estimated_hours","actual_hours",
            "created_by","assigned_to","tags","parent_task",
            "metadata","is_archived",
            "created_at","updated_at",
            "comments_count",
        ]
        read_only_fields = ["created_at","updated_at", "comments_count"]

class TeamSerializer(serializers.ModelSerializer):
    member_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Team._meta.get_field("members").remote_field.model.objects.all(),
        source="members",
        required=False,
    )

    class Meta:
        model = Team
        fields = ["id", "name", "members", "member_ids", "created_at"]
        read_only_fields = ["created_at"]