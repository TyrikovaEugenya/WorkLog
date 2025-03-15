from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу
        else:
            # Обработка ошибки аутентификации
            return render(request, 'users/login.html', {'error': 'Неверные учетные данные'})

    return render(request, 'users/login.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

