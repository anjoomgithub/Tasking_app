# api/serializers.py
from rest_framework import serializers
from .models import App, Task
from accounts.serializers import UserSerializer


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'name', 'icon', 'link', 'category', 'sub_category', 'points')


class TaskSerializer(serializers.ModelSerializer):
    # Use nested serializers for read-only representations
    user = UserSerializer(read_only=True)
    app = AppSerializer(read_only=True)

    # Use PrimaryKeyRelatedField for write operations
    app_id = serializers.PrimaryKeyRelatedField(
        queryset=App.objects.all(), source='app', write_only=True
    )

    class Meta:
        model = Task
        fields = ('id', 'user', 'app', 'app_id', 'screenshot', 'status', 'created_at')
        read_only_fields = ('status', 'user', 'app')  # 'app' is read-only because we use 'app_id' for writing