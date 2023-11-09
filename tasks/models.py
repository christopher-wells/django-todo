from django.urls import reverse
from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    task_complete = models.BooleanField(default=False)
    date_task_added = models.DateTimeField(auto_now_add=True)
    date_task_completed = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.task_name
    
    class Meta:
        ordering = ["date_task_added"]

    def get_absolute_url(self):
        return reverse('tasks:index')