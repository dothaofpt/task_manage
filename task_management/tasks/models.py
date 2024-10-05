
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('high', 'Cao'),
        ('medium', 'Trung bình'),
        ('low', 'Thấp'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Liên kết đến người dùng

    def __str__(self):
        return self.title
