from django.shortcuts import render

# Create your views here.

def render(request):
    return render(request, 'store/home.html')