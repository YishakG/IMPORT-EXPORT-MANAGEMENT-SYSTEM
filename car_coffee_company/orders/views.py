from django.shortcuts import render
from django.http import HttpResponse
from orders.models import *
import random

def generate_random_integer():
    return random.randint(100000, 999999)

def purchase(request):
    if request.method == 'POST':
        model = request.POST['model']
        year = request.POST['year']
        price = request.POST['price']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        color = request.POST['color']
        date = request.POST['delivery_date']
        my = Buy(Model= model,
                 Year=year,
                 Price=price,
                 Name=name,
                 Email=email,
                 PhoneNumber=phone,
                 Location=address,
                 Color=color,
                 Date=date,
                 )
        my.save()
        return HttpResponse("Order Saved Successfully")
    else:
        return render(request,"core/orders.html")
def imports(request):
    if request.method == 'POST':
        print("entered the if")
        name = request.POST['user_name']
        email = request.POST['email']
        model = request.POST['model']
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
    

        

