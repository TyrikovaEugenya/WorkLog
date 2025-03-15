from django.urls import path
from . import views

urlpatterns = [
    path('add_worklog/', views.add_worklog, name='add_worklog'),
    path('create_report', views.generate_report, name='create_report')
]