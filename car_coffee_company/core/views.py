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

# def home(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 from core.models import User  # Replace 'yourapp' with the name of your app
#                 if isinstance(user, User):
#                     print("Custom user model authenticated successfully.")
#                 else:
#                     print("The authenticated user is not an instance of the custom user model.")
#                 print("hell0")
#                 login(request, user)
#                 print(user.user_type)
#                 return redirect_user_based_on_type(user)
#             else:
#                 return render(request, 'core/home.html', {'form': form, 'error': 'Invalid login details'})
#     else:
#         form = LoginForm()
#     return render(request, 'core/home.html', {'form': form})
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


# Create your views here.


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

@login_required
def compliance_officer_home(request):
    return render(request, 'core/compliance_officer_home.html')

@login_required
def car_store_manager_home(request):
    return render(request, 'core/car_store_manager_home.html')

@login_required
def coffee_store_manager_home(request):
    return render(request, 'core/coffee_store_manager_home.html')

# @method_decorator(csrf_protect, name='dispatch')
# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         print(user)
#         if user is not None:
#             login(request, user)
#             if user.user_type == 'importer':
#                 return redirect('importer_home')
#             elif user.user_type == 'exporter':
#                 return redirect('exporter_home')
#             elif user.user_type == 'admin':
#                 return redirect('administrator_home')
#             elif user.user_type == 'finance_manager':
#                 return redirect('finance_manager_home')
#             elif user.user_type == 'compliance_officer':
#                 return redirect('compliance_officer_home')
#             elif user.user_type == 'car_store_manager':
#                 return redirect('car_store_manager_home')
#             elif user.user_type == 'coffee_store_manager':
#                 return redirect('coffee_store_manager_home')
#             else:
#                 return redirect('SIEMS_home')
#         else:
#             return redirect('SIEMS_home')
#     else:
#         return render(request, 'core/home.html')
