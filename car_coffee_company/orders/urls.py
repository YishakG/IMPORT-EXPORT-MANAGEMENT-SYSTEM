# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.purchase, name='submit_order'),  # Example URL pattern
    # Other URL patterns for the 'orders' app
]
