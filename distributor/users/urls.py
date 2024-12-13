from django.urls import path
from .views import RegisterCommonUserView, RegisterEmployeeAdminView, LoginView

urlpatterns = [
    # Rutas para registro
    path('register/common/', RegisterCommonUserView.as_view(), name='register_common_user'),
    path('register/employee-admin/', RegisterEmployeeAdminView.as_view(), name='register_employee_admin'),
    
    # Ruta para login
    path('login/', LoginView.as_view(), name='login'),
]
