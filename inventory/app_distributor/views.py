# app_distributor/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserLoginForm



# Vistas para la creacion y inicio de secion del usuario

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "¡Registro exitoso!")
            return redirect('home')  # Cambia 'home' a la vista a la que quieras redirigir
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "¡Inicio de sesión exitoso!")
                return redirect('home')  # Cambia 'home' a la vista a la que quieras redirigir
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})
