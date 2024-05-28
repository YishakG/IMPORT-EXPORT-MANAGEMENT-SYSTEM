from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Coffee, ImportTransaction, ExportTransaction
from .forms import CarForm, CoffeeForm, ImportTransactionForm, ExportTransactionForm

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'car_form.html', {'form': form})

# Similar views for coffee, import transactions, and export transactions...


# Create your views here.
