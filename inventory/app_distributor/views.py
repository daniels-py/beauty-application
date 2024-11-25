# app_distributor/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.db import DatabaseError
from django.forms import ValidationError
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from app_distributor.models import *
from django.views import View
import json
from .forms import * 



# redireccionamiento para las vista por defecto de mi app 
def admin_dashboard_view(request):
    return render(request, 'admin/admin_dashboard.html', {'active_page': 'dashboard'})

def admin_categorias_view(request):
     # Esta línea pasa un diccionario al contexto del template,
    # donde 'active_page' se establece como 'categorias'.
    # Esto permite al template saber qué enlace del menú debe tener la clase 'active',
    # indicando al usuario en qué sección de la aplicación se encuentra.
    return render(request, 'admin/admin_categorias.html',{'active_page': 'categorias'})


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
            return redirect('login')  # Cambia 'home' a la vista a la que quieras redirigir
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





# CRUD y consumo de APIS Categorias
@method_decorator(csrf_exempt, name='dispatch')
class ListarCategorias(View):
    def get(self, request):
        try:
            nombre = request.GET.get('nombre')
            categorias = Categoria.objects.all()

            if nombre:
                categorias = categorias.filter(nombre__icontains=nombre)

            # Validación del número de página
            page_number = self._get_page_number(request)
            page_size = self._get_page_size(request)

            paginator = Paginator(categorias, page_size)
            page_obj = paginator.get_page(page_number)

            datos_categorias = [
                {
                    'id': categoria.id,
                    'nombre': categoria.nombre,
                    'descripcion': categoria.descripcion,
                    'permite_color': categoria.permite_color
                }
                for categoria in page_obj
            ]

            if not datos_categorias:
                return JsonResponse({'message': 'No hay categorías disponibles'}, status=404)

            return JsonResponse({
                'categorias': datos_categorias,
                'page': page_obj.number,
                'pages': paginator.num_pages,
                'total': paginator.count
            })

        except DatabaseError as db_err:
            return JsonResponse({'error': 'Error en la base de datos: ' + str(db_err)}, status=500)
        except Exception as e:
            return JsonResponse({'error': 'Error interno: ' + str(e)}, status=500)

    def _get_page_number(self, request):
        try:
            return int(request.GET.get('page', 1))
        except (ValueError, TypeError):
            return 1

    def _get_page_size(self, request):
        try:
            return min(int(request.GET.get('page_size', 10)), 100)  # Límite de 100 por página
        except (ValueError, TypeError):
            return 10  # Valor predeterminado
