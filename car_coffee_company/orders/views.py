from django.shortcuts import render
from django.http import HttpResponse
from orders.models import Buy
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
# Create your views here.
