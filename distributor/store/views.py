from django.shortcuts import render
from django.views import View

class RegisterUserView(View):
    """
    Vista para renderizar la plantilla de registro de usuario común.
    """
    def get(self, request):
        return render(request, 'store/register.html')
