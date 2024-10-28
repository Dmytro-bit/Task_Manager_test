from django.db import models

from users.models import User


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.PositiveIntegerField()
    users = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
