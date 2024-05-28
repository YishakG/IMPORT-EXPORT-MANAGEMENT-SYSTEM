from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    vin = models.CharField(max_length=17, unique=True)
    import_date = models.DateField()

class Coffee(models.Model):
    variety = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    export_date = models.DateField()

class ImportTransaction(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    import_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

class ExportTransaction(models.Model):
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    export_date = models.DateField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)

