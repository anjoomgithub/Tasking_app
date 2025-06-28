# api/models.py
from django.db import models
from accounts.models import CustomUser

class App(models.Model):
    name = models.CharField(max_length=100)
    # Adding null=True and blank=True prevents migration errors if the db already exists
    icon = models.ImageField(upload_to='app_icons/', null=True, blank=True)
    link = models.URLField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    sub_category = models.CharField(max_length=50, null=True, blank=True)
    points = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('REJECTED', 'Rejected'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # A user can only submit a task for a specific app once
        unique_together = ('user', 'app')

    def __str__(self):
        return f'{self.user.username} - {self.app.name}'