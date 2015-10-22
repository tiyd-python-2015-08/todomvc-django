from rest_framework import serializers
from .models import Todo, Project
from django.contrib.auth.models import User

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Todo
        fields = ('id', 'title', 'completed', 'order', 'project', 'url')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    todo_set = serializers.StringRelatedField(many=True)
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Project
        fields = ('id', 'title', 'todo_set', 'owner')
