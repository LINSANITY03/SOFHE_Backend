
from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    date_only = serializers.DateTimeField(
        source="task_datetime", format="%Y-%m-%d")
    time_only = serializers.DateTimeField(
        source="task_datetime", format="%H:%M")

    class Meta:
        model = Event
        fields = ['id', 'title',
                  'description',
                  'task_datetime',
                  'status',
                  'date_only',
                  'time_only',
                  'credit']
