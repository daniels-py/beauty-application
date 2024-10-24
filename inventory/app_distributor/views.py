# app_distributor/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import *
from django.shortcuts import render, redirect


# redireccionamiento para las vista por defecto de mi app 
def admin_dashboard_view(request):
    return render(request, 'admin_dashboard.html')

def employee_dashboard_view(request):
    return render(request, 'employee_dashboard.html')

def Logout_View(request):
    logout(request) 
    return redirect('login')

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
                
                # Verifica el rol del usuario y redirige a la pantalla correspondiente
                if user.role == 'admin':
                    return redirect('admin_dashboard')  # Vista para administradores
                elif user.role == 'employee':
                    return redirect('employee_dashboard')  # Vista para empleados
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})




