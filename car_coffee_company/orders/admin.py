from django.contrib import admin
from .models import User
from .models import Order
from .models import Document
from .models import Shipment

admin.site.register(Order)
admin.site.register(Document)
admin.site.register(Shipment)

# Register your models here.
