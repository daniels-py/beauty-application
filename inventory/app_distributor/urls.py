# app_distributor/urls.py
from django.urls import path
from .views import *

urlpatterns = [

    # vistas de inicio 
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),

    # cerrar secion 
    path('logout/', Logout_View, name='logout'),

    # vistas dedicadas 
    path('admin_dashboard/', admin_dashboard_view, name='admin_dashboard'),
    path('employee_dashboard/', employee_dashboard_view, name='employee_dashboard'),
]
