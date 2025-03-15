from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TimeEntry
from projects.models import Project
from django.db.models import Sum


@login_required
def add_worklog(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        date = request.POST.get('date')
        hours = request.POST.get('hours')

        # Создание записи о времени
        TimeEntry.objects.create(
            user=request.user,
            project_id=project_id,
            date=date,
            hours=hours
        )
        return redirect('add_time')  # Перенаправление на страницу добавления времени

    projects = Project.objects.all()
    return render(request, 'add_time.html', {'projects': projects})

@login_required
def generate_report(request):
    if request.method == 'GET':
        project_id = request.GET.get('project_id')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        # Проверка, является ли пользователь менеджером
        if request.user.is_manager:
            report = (
                TimeEntry.objects
                .filter(project_id=project_id, date__gte=start_date, date__lt=end_date)
                .values('user_id')
                .annotate(hours=Sum('hours'))
            )
            return render(request, 'create_report.html', {'report': report})

    projects = Project.objects.all()
    return render(request, 'create_report.html', {'projects': projects})