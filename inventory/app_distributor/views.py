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
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from app_distributor.models import *
from django.views import View
import json
from .forms import * 


# redireccionamiento para las vista por defecto de mi app 
def admin_dashboard_view(request):
    return render(request, 'admin/admin_dashboard.html')

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



# CRUD y consumo de APIS



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

@method_decorator(csrf_exempt, name='dispatch')
class CrearCategoria(View):
    def post(self, request):
        return self.crear_categoria(request)

    def crear_categoria(self, request):
        try:
            data = json.loads(request.body)
            nueva_categoria = Categoria.objects.create(
                nombre=data['nombre'],
                descripcion=data['descripcion'],
                permite_color=data.get('permite_color', False)  # Default a False si no se proporciona
            )
            return JsonResponse({'id': nueva_categoria.id, 'nombre': nueva_categoria.nombre, 'descripcion': nueva_categoria.descripcion}, status=201)
        except (KeyError, ValueError) as e:
            return JsonResponse({'error': str(e)}, status=400)
        except DatabaseError:
            return JsonResponse({'error': 'Error al crear la categoría'}, status=500)
        except ValidationError as e:
            return JsonResponse({'error': e.messages}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class ListarMarcas(View):
    def get(self, request):
        try:
            marcas = Marca.objects.all()

            # Estructura de datos más detallada
            datos_marcas = {
                'marcas': [
                    {
                        'id': marca.id,
                        'nombre': marca.nombre,
                        'productos_count': marca.productos.count(),
                        'descripcion': marca.descripcion if hasattr(marca, 'descripcion') else 'Descripción no disponible',  # Suponiendo que tienes un campo descripción en Marca
                    }
                    for marca in marcas
                ]
            }

            if not datos_marcas['marcas']:
                return JsonResponse({'message': 'Marcas no disponibles.'}, status=404)

            return JsonResponse(datos_marcas, status=200)

        except DatabaseError:
            return JsonResponse({'error': 'Error al obtener las marcas.'}, status=500)
        
@method_decorator(csrf_exempt, name='dispatch')
class CrearMarca(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')

            if not nombre:
                return JsonResponse({'error': 'El nombre es obligatorio.'}, status=400)

            marca = Marca(nombre=nombre)
            marca.save()
            return JsonResponse({'message': 'Marca creada con éxito.', 'id': marca.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos.'}, status=400)
        except DatabaseError:
            return JsonResponse({'error': 'Error al crear la marca.'}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class ListarPresentaciones(View):
    def get(self, request):
        try:
            presentaciones = Presentacion.objects.all()

            # Estructura de datos más detallada
            datos_presentaciones = {
                'presentaciones': [
                    {
                        'id': presentacion.id,
                        'nombre': presentacion.nombre,
                        'productos_asociados_count': presentacion.productos.count(),
                        'descripcion': presentacion.descripcion if hasattr(presentacion, 'descripcion') else 'Descripción no disponible',  # Suponiendo que tienes un campo descripción en Presentacion
                    }
                    for presentacion in presentaciones
                ]
            }

            if not datos_presentaciones['presentaciones']:
                return JsonResponse({'mensaje': 'Presentaciones no disponibles'}, status=404)

            return JsonResponse(datos_presentaciones, status=200)

        except DatabaseError:
            return JsonResponse({'error': 'Error al obtener las presentaciones'}, status=500)
@method_decorator(csrf_exempt, name='dispatch')
class CrearPresentacion(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            if not nombre:
                return JsonResponse({'error': 'El nombre es obligatorio'}, status=400)

            presentacion = Presentacion.objects.create(nombre=nombre)
            return JsonResponse({'id': presentacion.id, 'nombre': presentacion.nombre}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos'}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class ListarCartasColor(View):
    def get(self, request):
        try:
            # Obtener todas las cartas de color junto con las marcas relacionadas
            cartas_color = CartaColor.objects.select_related('marca').all()

            # Crear un diccionario para agrupar las cartas de color por marca
            cartas_por_marca = {}
            for cc in cartas_color:
                marca_nombre = cc.marca.nombre
                if marca_nombre not in cartas_por_marca:
                    cartas_por_marca[marca_nombre] = []
                cartas_por_marca[marca_nombre].append({
                    'id': cc.id,
                    'nombre_color': cc.nombre_color,
                    'codigo_color': cc.codigo_color,
                    'hexadecimal': cc.hexadecimal,
                    'descripcion': cc.descripcion
                })

            # Convertir el diccionario en una lista de marcas con sus cartas
            cartas_de_color = [
                {
                    'marca': marca,
                    'cartas': cartas
                }
                for marca, cartas in cartas_por_marca.items()
            ]

            # Si no hay datos, devolver un mensaje
            if not cartas_de_color:
                return JsonResponse({'mensaje': 'Cartas de color no disponibles'}, status=404)

            # Devolver el JSON con la estructura deseada
            return JsonResponse({'cartas_de_color': cartas_de_color}, safe=False, status=200)

        except DatabaseError:
            return JsonResponse({'error': 'Error al obtener las cartas de color'}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class CrearCartaColor(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')
            marca_id = data.get('marca_id')

            if not nombre or not marca_id:
                return JsonResponse({'error': 'El nombre y la marca son obligatorios'}, status=400)

            carta_color = CartaColor.objects.create(nombre=nombre, marca_id=marca_id)
            return JsonResponse({'id': carta_color.id, 'nombre': carta_color.nombre, 'marca_id': carta_color.marca.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class ListarProductos(View):
    def get(self, request):
        try:
            productos = Producto.objects.select_related('categoria', 'marca').all()
            if not productos:
                return JsonResponse({'mensaje': 'Productos no disponibles'}, status=404)

            # Estructura de datos más detallada
            data = {
                'productos': [
                    {
                        'id': p.id,
                        'nombre': p.nombre,
                        'descripcion': p.descripcion,
                        'precio': str(p.precio),  # Asegúrate de que el precio sea un string si quieres formatearlo
                        'categoria': {
                            'id': p.categoria.id,
                            'nombre': p.categoria.nombre,
                            'permite_color': p.categoria.permite_color  # Agrega la opción permite_color
                        },
                        'marca': {
                            'id': p.marca.id,
                            'nombre': p.marca.nombre,
                            'productos_count': p.marca.productos.count()  # Contador de productos asociados
                        },
                        'carta_color': {
                            'id': p.carta_color.id if p.carta_color else None,
                            'codigo_color': p.carta_color.codigo_color if p.carta_color else None,
                            'nombre_color': p.carta_color.nombre_color if p.carta_color else None,
                        }
                    } for p in productos
                ]
            }

            return JsonResponse(data, status=200)

        except DatabaseError:
            return JsonResponse({'error': 'Error al obtener los productos'}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class ListarInventario(View):
    def get(self, request):
        try:
            inventarios = Inventario.objects.select_related('producto__presentacion', 'producto__categoria', 'producto__marca').all()
            if not inventarios:
                return JsonResponse({'mensaje': 'Inventario no disponible'}, status=404)

            productos_disponibles = [
                {
                    'id': inv.id,
                    'producto': inv.producto.nombre,
                    'categoria': inv.producto.categoria.nombre,
                    'marca': inv.producto.marca.nombre,
                    'presentacion': inv.producto.presentacion.nombre,
                    'unidades': inv.unidades
                }
                for inv in inventarios
            ]

            return JsonResponse({'productos_disponibles': productos_disponibles}, status=200)

        except DatabaseError:
            return JsonResponse({'error': 'Error al obtener el inventario'}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class CrearInventario(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            producto_id = data.get('producto_id')
            unidades = data.get('unidades', 0)

            if not producto_id:
                return JsonResponse({'error': 'El ID del producto es obligatorio.'}, status=400)

            try:
                producto = Producto.objects.get(id=producto_id)
            except Producto.DoesNotExist:
                return JsonResponse({'error': 'El producto no existe.'}, status=404)

            inventario, creado = Inventario.objects.get_or_create(producto=producto)
            inventario.unidades = unidades
            inventario.save()

            mensaje = 'Producto añadido al inventario.' if creado else 'Inventario actualizado.'
            return JsonResponse({'message': mensaje, 'producto_id': producto.id, 'unidades': inventario.unidades}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos.'}, status=400)
        except DatabaseError:
            return JsonResponse({'error': 'Error al crear o actualizar el inventario.'}, status=500)