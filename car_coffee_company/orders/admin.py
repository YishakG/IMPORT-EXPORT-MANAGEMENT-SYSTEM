from django.contrib import admin
from .models import User
from .models import Order
from .models import Document
from .models import Shipment
from .models import Buy


admin.site.register(Order)
admin.site.register(Document)
admin.site.register(Shipment)
admin.site.register(Buy)


# Register your models here.
# python manage.py migrate <your_app_name> zero
# python manage.py migrate --fake-initial
