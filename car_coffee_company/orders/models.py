# Create your models here.
from django.db import models
# import random
from core.models import User

# def generate_random_integer():
#     return random.randint(100000, 999999)

class Order(models.Model):
    ORDER_TYPES = (
        ('import', 'Import'),
        ('export', 'Export'),
        
    )
    order_type = models.CharField(max_length=10, choices=ORDER_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()
    delivery_date = models.DateField()
    status = models.CharField(max_length=20, default='pending')

class importOrder(models.Model):
    # Name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    TrackingNo = models.IntegerField(primary_key=True,unique=True,blank=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(default='example@example.com')
    Model = models.CharField(max_length=100, default='Anonymous')
    Specifications = models.CharField(max_length=100, default='Anonymous')
    Color = models.CharField(max_length=50, default='Unspecified')
    Year = models.CharField(max_length=4, default='2023')
    Price = models.PositiveIntegerField()
    Date =  models.DateField(null=True, blank=True)
    Count = models.PositiveIntegerField()
     
    
class Buy(models.Model):
    id = models.AutoField(primary_key=True)
    Model = models.CharField(max_length=100, default='Anonymous')
    Year = models.CharField(max_length=4, default='2023')
    Price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Name = models.CharField(max_length=100, default='Anonymous')
    Email = models.EmailField(default='example@example.com')
    PhoneNumber = models.CharField(max_length=20, default='00-0000-0000')
    Location = models.CharField(max_length=50,default='Unknown Address')
    Color = models.CharField(max_length=50, default='Unspecified')
    Date =  models.DateField(null=True, blank=True) 
    def __str__(self):
        return self.Name

class Document(models.Model):
    DOCUMENT_TYPES = (
        ('invoice', 'Invoice'),
        ('bill_of_lading', 'Bill of Lading'),
        ('certificate_of_origin', 'Certificate of Origin'),
        ('packing_list', 'Packing List'),
        ('customs_declaration', 'Customs Declaration'),
    )
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPES)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Shipment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='shipments')
    tracking_number = models.CharField(max_length=50)
    carrier = models.CharField(max_length=50)
    departure_date = models.DateField()
    arrival_date = models.DateField()
    status = models.CharField(max_length=20, default='in_transit')
