from django.shortcuts import render
from django.views import View


def Home(request):
    return render(request, "store/pages/home.html")



class RegisterUserView(View):
    """
    Vista para renderizar la plantilla de registro de usuario común.
    """
    def get(self, request):
        return render(request, 'store/auth/register.html')
