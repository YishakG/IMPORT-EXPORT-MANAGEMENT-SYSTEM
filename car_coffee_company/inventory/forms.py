from django import forms
from .models import Car, Coffee, ImportTransaction, ExportTransaction

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = '__all__'

class ImportTransactionForm(forms.ModelForm):
    class Meta:
        model = ImportTransaction
        fields = '__all__'

class ExportTransactionForm(forms.ModelForm):
    class Meta:
        model = ExportTransaction
        fields = '__all__'
