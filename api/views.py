# api/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import App, Task, CustomUser
from .serializers import AppSerializer, TaskSerializer

# --- Admin Views ---
class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class AdminAppListCreateView(generics.ListCreateAPIView):
    queryset = App.objects.all().order_by('-id')
    serializer_class = AppSerializer
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

class AdminTaskListView(generics.ListAPIView):
    queryset = Task.objects.filter(status='PENDING').order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser]

class AdminTaskApproveView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.status == 'PENDING':
            task.status = 'COMPLETED'
            task.user.points += task.app.points
            task.user.save()
            task.save()
            return Response(self.get_serializer(task).data)
        return Response({'error': 'Task is not in a pending state.'}, status=status.HTTP_400_BAD_REQUEST)

# --- User Views ---
class UserAppListView(generics.ListAPIView):
    serializer_class = AppSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Get IDs of apps for which the user has already submitted a task
        submitted_app_ids = Task.objects.filter(user=user).values_list('app_id', flat=True)
        # Return apps that are NOT in the submitted list
        return App.objects.exclude(id__in=submitted_app_ids).order_by('-id')

class UserTaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserTaskHistoryView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')