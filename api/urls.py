# api/urls.py
from django.urls import path
from .views import (
    AdminAppListCreateView,
    AdminTaskListView,
    AdminTaskApproveView,
    UserAppListView,
    UserTaskCreateView,
    UserTaskHistoryView,
)

urlpatterns = [
    # Admin URLs
    path('admin/apps/', AdminAppListCreateView.as_view(), name='admin-app-list-create'),
    path('admin/tasks/', AdminTaskListView.as_view(), name='admin-task-list'),
    path('admin/tasks/<int:pk>/approve/', AdminTaskApproveView.as_view(), name='admin-task-approve'),

    # User URLs
    path('apps/', UserAppListView.as_view(), name='user-app-list'),
    path('tasks/', UserTaskCreateView.as_view(), name='user-task-create'),
    path('tasks/history/', UserTaskHistoryView.as_view(), name='user-task-history'),
]