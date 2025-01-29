from django.views import View
from django.shortcuts import render


# clases que maneja vista del panel de control
class DashboardView(View):
    def get(self, request):
        context = {'active_page': 'dashboard', 'page_title': 'Dashboard'}
        return render(request, 'dashboard/admin/dashboard.html', context)
    

class usersView(View):
    def get(self, request):
        context = {'active_page': 'users', 'page_title': 'Users'}
        return render(request, 'dashboard/admin/users.html', context)


class productsView(View):
    def get(self, request):
        context = {'active_page': 'products', 'page_title': 'Products'}
        return render(request, 'dashboard/admin/products.html', context)
    

    


def admin_dashboard(request):
    return render(request, 'dashboard/admin/dashboard.html')

def employee_dashboard(request):
    return render(request, 'dashboard/employee/employee_dashboard.html')


def plantilla_base(request):
    context = {'plantilla_base'}
    return render (request, 'dashboard/admin/base.html')