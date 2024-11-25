# app_distributor/views.py
from sqlite3 import DatabaseError
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from app_distributor.models import *
from .forms import * 
from .serializers import *
from rest_framework import generics
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


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



# Vistas para las Categorías framework django rest end point

# Definición de la paginación
class CategoriaPagination(PageNumberPagination):
    page_size = 10  # Número de elementos por página
    page_size_query_param = 'page_size'  # Parámetro para especificar el tamaño de la página
    max_page_size = 100  # Máximo número de elementos por página

# Vista para listar y crear categorías con paginación
class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    pagination_class = CategoriaPagination  # Aplica la paginación a esta vista

    def get(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()  # Obtiene todas las categorías
            if not queryset.exists():  # Verifica si hay categorías
                return Response({"categorias": [], "message": "No existen datos registrados"}, status=404)

            paginator = self.pagination_class()  # Crea una instancia del paginador
            page_obj = paginator.paginate_queryset(queryset, request)  # Aplica la paginación

            # Si hay una página, serializa los datos y devuelve la respuesta con paginación
            if page_obj is not None:
                serializer = self.get_serializer(page_obj, many=True)
                return paginator.get_paginated_response({"categorias": serializer.data})

            # Si no hay paginación, simplemente devuelve todos los datos dentro de "categorias"
            serializer = self.get_serializer(queryset, many=True)
            return Response({"categorias": serializer.data, "total": queryset.count()})

        except DatabaseError as db_err:
            return Response({"error": f"Error en la base de datos: {str(db_err)}"}, status=500)
        except Exception as e:
            return Response({"error": f"Error interno: {str(e)}"}, status=500)
