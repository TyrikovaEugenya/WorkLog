from django.shortcuts import render
from django.db.models import Sum
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import TimeEntry
from .serializers import TimeEntrySerializer, ReportSerializer
from projects.models import Project


class TimeEntryViewSet(viewsets.ModelViewSet):
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer

    @action(detail=False, methods=['GET'])
    def report(self, request):
        project_id = request.query_params.get('project_id')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        
        # Проверка прав (только менеджер проекта)
        project = Project.objects.get(id=project_id)
        if request.user != project.manager:
            return Response({'error': 'Доступ запрещен'}, status=403)
        
        # Формирование отчета
        entries = TimeEntry.objects.filter(
            project=project_id,
            date__gte=start_date,
            date__lt=end_date
        ).values('user').annotate(total_hours=Sum('hours'))
        
        report_data = [
            {'id': entry['user'], 'hours': entry['total_hours']}
            for entry in entries
        ]
        
        serializer = ReportSerializer(report_data, many=True)
        return Response(serializer.data)
