from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage_projects, name='manage_projects')
]
