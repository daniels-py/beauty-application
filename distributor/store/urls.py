from django.urls import path
from .views import RegisterUserView
from .views import*

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('Home/', Home, name="Home" ),
]
