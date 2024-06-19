from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import LoginForm
from .models import User
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from core.models import User
from core.backends import CustomUserBackend
from orders.views import *
from orders.models import *

    
def redirect_user_based_on_type(user):
    if user.user_type == 'importer':
        return redirect('core/importer_home')
    elif user.user_type == 'exporter':
        return redirect('core/exporter_home')
    elif user.user_type == 'admin':
        return redirect('core/admin_home')
    elif user.user_type == 'accountant':
        return redirect('core/accountant_home')
    elif user.user_type == 'finance_manager':
        return redirect('core/finance_manager_home')
    elif user.user_type == 'compliance_officer':
        return redirect('core/compliance_officer_home')
    elif user.user_type == 'car_store_manager':
        return redirect('core/car_store__home')
    elif user.user_type == 'coffee_store_manager':
        return redirect('core/coffee_store_home')
        # Add more user type checks and redirects here
    else:
        return HttpResponse("User type not recognized")

def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print(f"Authenticated user: {user.username} - {user.user_type}")  # Debugging print
                login(request, user)
                print(user.user)
                return redirect_user_based_on_type(user)
            else:
                return render(request, 'core/home.html', {'form': form, 'error': 'Invalid login details'})
    else:
        form = LoginForm()
    return render(request, 'core/home.html', {'form': form})
def about_view(request):
    return render(request, 'core/about.html')

def cars(request):
    return render(request, 'core/cars.html')

def orders(request):
    return render(request, 'core/orders.html')

@login_required
def importer_home(request):
    return render(request, 'core/importer_home.html')

@login_required
def exporter_home(request):
    return render(request, 'core/exporter_home.html')

@login_required
def administrator_home(request):
    return render(request, 'core/administrator_home.html')

@login_required
def finance_manager_home(request):
    return render(request, 'core/finance_manager_home.html')

def finance_available(request):
    return render(request, 'core/financeAvailable.html')

def finance_import(request):
    return render(request, 'core/financeImport.html')

def finance_sell(request):
    return render(request, 'core/financeSell.html')

@login_required
def compliance_officer_home(request):
    return render(request, 'core/compliance_officer_home.html')

@login_required
def car_store_manager_home(request):
    return render(request, 'core/car_store_manager_home.html')

@login_required
def coffee_store_manager_home(request):
    return render(request, 'core/coffee_store_manager_home.html')
@login_required
def shipments_home(request):
    return render(request, 'core/shipment.html')

def imports(request):
    if request.method == 'POST':
        print("entered the if")
        name = request.POST['name']
        email = request.POST['email']
        model = request.POST['carModel']
        specifications = request.POST['specifications']
        color = request.POST['color']
        year = request.POST['year']
        price = request.POST['price']
        date = request.POST['orderDate']
        count = request.POST['count']
        print("before trackingno")
        trackingno = generate_random_integer()
        my = importOrder(
            TrackingNo = trackingno,
            Name = name,
            Email = email,
            Model = model,
            Specifications = specifications,
            Color = color,
            Year = year,
            Price = price,
            Date = date,
            Count = count,
                      )
        my.save()

        print('after my.save')
        return HttpResponse("Import Order Saved Successfully")
    else:
        print('entered else')
        return render(request,"core/importOrders.html")
def get_import(request):
    import_orders = importOrder.objects.all()
    return render(request, 'core/financeImport.html', {'import_orders': import_orders})
    
 