from django.contrib import admin

from .models import FinancialTransaction
from .models import TaxRecord

admin.site.register(FinancialTransaction)
admin.site.register(TaxRecord)
# Register your models here.
