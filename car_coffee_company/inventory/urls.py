from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_list, name='car_list'),
    path('cars/new/', views.car_create, name='car_create'),
    # Add similar paths for coffee, import transactions, and export transactions
]
