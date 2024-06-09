from django.db import models

from orders.models import Order

# Create your models here.
class FinancialTransaction(models.Model):
    TRANSACTION_TYPES = (
        ('payment', 'Payment'),
        ('refund', 'Refund'),
        ('fee', 'Fee'),
        ('tax', 'Tax'),
    )
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
class TaxRecord(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='tax_records')
    tax_type = models.CharField(max_length=50)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_date = models.DateField()
