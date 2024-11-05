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

# Contador general
def get_dashboard_counts(request):
    user_count = get_user_model().objects.count()  # Contar usuarios
    categoria_count = Categoria.objects.count()  # Contar categorías
    marca_count = Marca.objects.count()  # Contar marcas
    presentacion_count = Presentacion.objects.count()  # Contar presentaciones
    carta_color_count = CartaColor.objects.count()  # Contar cartas de color
    producto_count = Producto.objects.count()  # Contar productos
    inventario_count = Inventario.objects.count()  # Contar inventario

    data = {
        'user_count': user_count,
        'categoria_count': categoria_count,
        'marca_count': marca_count,
        'presentacion_count': presentacion_count,
        'carta_color_count': carta_color_count,
        'producto_count': producto_count,
        'inventario_count': inventario_count,
    }
    return JsonResponse(data)

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
class ActualizarCategoria(View):
    def post(self, request, id):
        try:
            data = json.loads(request.body)
            categoria = Categoria.objects.get(id=id)

            categoria.nombre = data.get('nombre', categoria.nombre)
            categoria.descripcion = data.get('descripcion', categoria.descripcion)
            categoria.permite_color = data.get('permite_color', categoria.permite_color)
            categoria.save()

            return JsonResponse({'message': 'Categoría actualizada con éxito.'}, status=200)

        except Categoria.DoesNotExist:
            return JsonResponse({'error': 'Categoría no encontrada.'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos.'}, status=400)
        except DatabaseError:
            return JsonResponse({'error': 'Error al actualizar la categoría.'}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class EliminarCategoria(View):
    def delete(self, request, id):
        try:
            categoria = Categoria.objects.get(id=id)
            categoria.delete()
            return JsonResponse({'message': 'Categoría eliminada con éxito.'}, status=200)
        except Categoria.DoesNotExist:
            return JsonResponse({'error': 'Categoría no encontrada.'}, status=404)
        except DatabaseError:
            return JsonResponse({'error': 'Error al eliminar la categoría.'}, status=500)



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
class ActualizarMarca(View):
    def post(self, request, id):
        try:
            data = json.loads(request.body)
            marca = Marca.objects.get(id=id)

            marca.nombre = data.get('nombre', marca.nombre)
            marca.save()

            return JsonResponse({'message': 'Marca actualizada con éxito.'}, status=200)

        except Marca.DoesNotExist:
            return JsonResponse({'error': 'Marca no encontrada.'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos.'}, status=400)
        except DatabaseError:
            return JsonResponse({'error': 'Error al actualizar la marca.'}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class EliminarMarca(View):
    def delete(self, request, id):
        try:
            marca = Marca.objects.get(id=id)
            marca.delete()
            return JsonResponse({'message': 'Marca eliminada con éxito.'}, status=200)
        except Marca.DoesNotExist:
            return JsonResponse({'error': 'Marca no encontrada.'}, status=404)
        except DatabaseError:
            return JsonResponse({'error': 'Error al eliminar la marca.'}, status=500)



@method_decorator(csrf_exempt, name='dispatch')
class ListarPresentaciones(View):
    def get(self, request):
        try:
            # Obtener todas las presentaciones
            presentaciones = Presentacion.objects.all()

            # Verificar si no hay presentaciones disponibles
            if not presentaciones:
                return JsonResponse({'mensaje': 'No hay presentaciones disponibles.'}, status=404)

            # Obtener el número de página de la solicitud (por defecto la página 1)
            page_number = request.GET.get('page', 1)

            # Definir el tamaño de la página (cuántos ítems mostrar por página)
            page_size = 10  # Puedes ajustar el número de elementos por página según sea necesario

            # Crear el paginador con el conjunto de presentaciones
            paginator = Paginator(presentaciones, page_size)

            # Obtener la página solicitada
            page_obj = paginator.get_page(page_number)

            # Estructura de datos para la respuesta
            data = {
                'presentaciones': [
                    {
                        'id': p.id,
                        'nombre': p.nombre
                    } for p in page_obj
                ],
                'paginacion': {
                    'pagina_actual': page_obj.number,
                    'total_paginas': paginator.num_pages,
                    'tiene_siguiente': page_obj.has_next(),
                    'tiene_anterior': page_obj.has_previous(),
                    'total_presentaciones': paginator.count
                }
            }

            return JsonResponse(data, status=200)

        except DatabaseError:
            return JsonResponse({'error': 'Error al obtener las presentaciones.'}, status=500)
        except ValueError:
            return JsonResponse({'error': 'Número de página inválido.'}, status=400)
@method_decorator(csrf_exempt, name='dispatch')
class CrearPresentacion(View):
    def post(self, request):
        try:
            # Cargar los datos JSON de la solicitud
            data = json.loads(request.body)

            # Validar que el nombre de la presentación esté presente
            nombre = data.get('nombre')
            if not nombre:
                return JsonResponse({'error': 'El nombre es obligatorio.'}, status=400)

            # Crear la nueva presentación
            presentacion = Presentacion.objects.create(nombre=nombre)

            # Devolver respuesta exitosa con los detalles de la nueva presentación
            return JsonResponse({
                'message': 'Presentación creada con éxito.',
                'presentacion': {
                    'id': presentacion.id,
                    'nombre': presentacion.nombre
                }
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos.'}, status=400)
        except DatabaseError:
            return JsonResponse({'error': 'Error al crear la presentación.'}, status=500)
@method_decorator(csrf_exempt, name='dispatch')
class ActualizarPresentacion(View):
    def post(self, request, id):
        try:
            data = json.loads(request.body)
            presentacion = Presentacion.objects.get(id=id)

            presentacion.nombre = data.get('nombre', presentacion.nombre)
            presentacion.save()

            return JsonResponse({'message': 'Presentación actualizada con éxito.'}, status=200)

        except Presentacion.DoesNotExist:
            return JsonResponse({'error': 'Presentación no encontrada.'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos.'}, status=400)
        except DatabaseError:
            return JsonResponse({'error': 'Error al actualizar la presentación.'}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class EliminarPresentacion(View):
    def delete(self, request, id):
        try:
            presentacion = Presentacion.objects.get(id=id)
            presentacion.delete()
            return JsonResponse({'message': 'Presentación eliminada con éxito.'}, status=200)
        except Presentacion.DoesNotExist:
            return JsonResponse({'error': 'Presentación no encontrada.'}, status=404)
        except DatabaseError:
            return JsonResponse({'error': 'Error al eliminar la presentación.'}, status=500)



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
class ActualizarCartaColor(View):
    def post(self, request, id):
        try:
            data = json.loads(request.body)
            carta_color = CartaColor.objects.get(id=id)

            carta_color.nombre_color = data.get('nombre_color', carta_color.nombre_color)
            carta_color.codigo_color = data.get('codigo_color', carta_color.codigo_color)
            carta_color.hexadecimal = data.get('hexadecimal', carta_color.hexadecimal)
            carta_color.descripcion = data.get('descripcion', carta_color.descripcion)
            carta_color.marca_id = data.get('marca_id', carta_color.marca_id)
            carta_color.save()

            return JsonResponse({'message': 'Carta de color actualizada con éxito.'}, status=200)

        except CartaColor.DoesNotExist:
            return JsonResponse({'error': 'Carta de color no encontrada.'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos.'}, status=400)
        except DatabaseError:
            return JsonResponse({'error': 'Error al actualizar la carta de color.'}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class EliminarCartaColor(View):
    def delete(self, request, id):
        try:
            carta_color = CartaColor.objects.get(id=id)
            carta_color.delete()
            return JsonResponse({'message': 'Carta de color eliminada con éxito.'}, status=200)
        except CartaColor.DoesNotExist:
            return JsonResponse({'error': 'Carta de color no encontrada.'}, status=404)
        except DatabaseError:
            return JsonResponse({'error': 'Error al eliminar la carta de color.'}, status=500)




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
class CrearProducto(View):
    def post(self, request):
        try:
            # Cargar y decodificar los datos JSON del cuerpo de la solicitud
            data = json.loads(request.body)

            # Validar los campos obligatorios
            nombre = data.get('nombre')
            descripcion = data.get('descripcion')
            precio = data.get('precio')
            categoria_id = data.get('categoria_id')
            marca_id = data.get('marca_id')

            # Asegurarse de que los campos obligatorios no estén vacíos
            if not nombre or not precio or not categoria_id or not marca_id:
                return JsonResponse({'error': 'Faltan campos obligatorios.'}, status=400)

            # Crear el producto y asignar los campos
            producto = Producto.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                categoria_id=categoria_id,
                marca_id=marca_id,
                carta_color_id=data.get('carta_color_id')  # Puede ser opcional
            )

            return JsonResponse({
                'message': 'Producto creado con éxito.',
                'producto': {
                    'id': producto.id,
                    'nombre': producto.nombre,
                    'descripcion': producto.descripcion,
                    'precio': str(producto.precio),
                    'categoria': {
                        'id': producto.categoria.id,
                        'nombre': producto.categoria.nombre
                    },
                    'marca': {
                        'id': producto.marca.id,
                        'nombre': producto.marca.nombre
                    },
                    'carta_color': {
                        'id': producto.carta_color.id if producto.carta_color else None,
                        'codigo_color': producto.carta_color.codigo_color if producto.carta_color else None,
                        'nombre_color': producto.carta_color.nombre_color if producto.carta_color else None,
                    }
                }
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos.'}, status=400)
        except Categoria.DoesNotExist:
            return JsonResponse({'error': 'Categoría no encontrada.'}, status=404)
        except Marca.DoesNotExist:
            return JsonResponse({'error': 'Marca no encontrada.'}, status=404)
        except DatabaseError:
            return JsonResponse({'error': 'Error al crear el producto.'}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class ActualizarProducto(View):
    def post(self, request, id):
        try:
            data = json.loads(request.body)
            producto = Producto.objects.get(id=id)

            producto.nombre = data.get('nombre', producto.nombre)
            producto.descripcion = data.get('descripcion', producto.descripcion)
            producto.precio = data.get('precio', producto.precio)
            producto.categoria_id = data.get('categoria_id', producto.categoria_id)
            producto.marca_id = data.get('marca_id', producto.marca_id)
            producto.carta_color_id = data.get('carta_color_id', producto.carta_color_id)
            producto.save()

            return JsonResponse({'message': 'Producto actualizado con éxito.'}, status=200)

        except Producto.DoesNotExist:
            return JsonResponse({'error': 'Producto no encontrado.'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos.'}, status=400)
        except DatabaseError:
            return JsonResponse({'error': 'Error al actualizar el producto.'}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class EliminarProducto(View):
    def delete(self, request, id):
        try:
            producto = Producto.objects.get(id=id)
            producto.delete()
            return JsonResponse({'message': 'Producto eliminado con éxito.'}, status=200)
        except Producto.DoesNotExist:
            return JsonResponse({'error': 'Producto no encontrado.'}, status=404)
        except DatabaseError:
            return JsonResponse({'error': 'Error al eliminar el producto.'}, status=500)



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
        
@method_decorator(csrf_exempt, name='dispatch')
class ActualizarInventario(View):
    def post(self, request, id):
        try:
            data = json.loads(request.body)
            inventario = Inventario.objects.get(id=id)

            inventario.unidades = data.get('unidades', inventario.unidades)
            inventario.save()

            return JsonResponse({'message': 'Inventario actualizado con éxito.'}, status=200)

        except Inventario.DoesNotExist:
            return JsonResponse({'error': 'Inventario no encontrado.'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos.'}, status=400)
        except DatabaseError:
            return JsonResponse({'error': 'Error al actualizar el inventario.'}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class EliminarInventario(View):
    def delete(self, request, id):
        try:
            inventario = Inventario.objects.get(id=id)
            inventario.delete()
            return JsonResponse({'message': 'Inventario eliminado con éxito.'}, status=200)
        except Inventario.DoesNotExist:
            return JsonResponse({'error': 'Inventario no encontrado.'}, status=404)
        except DatabaseError:
            return JsonResponse({'error': 'Error al eliminar el inventario.'}, status=500)

