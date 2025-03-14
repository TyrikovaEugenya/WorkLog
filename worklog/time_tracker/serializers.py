from rest_framework import serializers
from .models import TimeEntry

class TimeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeEntry
        fields = '__all__'

class ReportSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    hours = serializers.IntegerField()