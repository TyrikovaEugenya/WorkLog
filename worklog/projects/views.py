from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.decorators import login_required

@login_required
def manage_projects(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        Project.objects.create(name=project_name)
        return redirect('manage_projects')  # Перенаправление на страницу управления проектами

    projects = Project.objects.all()
    return render(request, 'manage_projects.html', {'projects': projects})
