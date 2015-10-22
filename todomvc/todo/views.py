from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Todo, Project
from .serializers import TodoSerializer, ProjectSerializer
# Create your views here.

from .permissions import IsOwner


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        try:
            return self.request.user.project_set.all()
        except AttributeError:
            return None
        # return Project.objects.all()
