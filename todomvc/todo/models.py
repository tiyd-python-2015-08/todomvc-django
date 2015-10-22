from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    order = models.IntegerField(null=True)
    project = models.ForeignKey('Project', null=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.title
