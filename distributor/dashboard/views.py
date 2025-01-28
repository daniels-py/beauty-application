from django.views import View
from django.shortcuts import render

def admin_dashboard(request):
    return render(request, 'dashboard/admin/dashboard.html')

def employee_dashboard(request):
    return render(request, 'dashboard/employee/employee_dashboard.html')


def plantilla_base(request):
    context = {'plantilla_base'}
    return render (request, 'dashboard/admin/base.html')