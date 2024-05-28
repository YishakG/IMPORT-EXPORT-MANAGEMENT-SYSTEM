from django.contrib import admin

# Register your models here.
from .models import Car, Coffee, ImportTransaction, ExportTransaction

admin.site.register(Car)
admin.site.register(Coffee)
admin.site.register(ImportTransaction)
admin.site.register(ExportTransaction)
