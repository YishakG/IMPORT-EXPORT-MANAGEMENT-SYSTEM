# Create your models here.
from django.db import models

from core.models import User

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