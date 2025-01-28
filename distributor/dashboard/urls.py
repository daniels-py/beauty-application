# filepath: /c:/Users/Danielito/Desktop/beauty-application/distributor/dashboard/urls.py
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('employee/', views.employee_dashboard, name='employee_dashboard'),

    path('admin/base/', plantilla_base, name='plantilla_base'),
    # otras rutas del dashboard
]