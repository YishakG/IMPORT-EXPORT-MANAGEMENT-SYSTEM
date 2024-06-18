# from django.urls import path, include
# from django.contrib.auth.views import LoginView
# from . import views

# urlpatterns = [
#     path('about/', views.about_view, name="SIEMS_about"),
#     path('', views.home , name="SIEMS_home"),
#     path('cars/', views.cars, name="SIEMS_cars"),
#     path('importer/', views.importer_home, name='importer_home'),
#     path('exporter/', views.exporter_home, name='exporter_home'),
#     # path('login/', LoginView.as_view(template_name='core/cars.html'), name='login'),
#     path('administrator/', views.administrator_home, name='administrator_home'),
#     path('finance_manager/', views.finance_manager_home, name='finance_manager_home'),
#     path('compliance_officer/', views.compliance_officer_home, name='compliance_officer_home'),
#     path('car_store_manager/', views.car_store_manager_home, name='car_store_manager_home'),
#     path('coffee_store_manager/', views.coffee_store_manager_home, name='coffee_store_manager_home'),
#     path('accounts/login/', views.login_user, name='login1'),  # Keep this one
#     path('accounts/', include('django.contrib.auth.urls')),
# ]

from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views
from orders import views as orders_views

urlpatterns = [
    path('about/', views.about_view, name="SIEMS_about"),
    path('', views.home, name="SIEMS_home"),
    path('cars/', views.cars, name="SIEMS_cars"),
    path('orders/', views.orders, name="SIEMS_orders"),
    path('submit_order/', include('orders.urls')),
    path('importer/', views.importer_home, name='importer_home'),
    path('exporter/', views.exporter_home, name='exporter_home'),
    path('administrator/', views.administrator_home, name='administrator_home'),
    path('finance_manager/', views.finance_manager_home, name='finance_manager_home'),
    path('compliance_officer/', views.compliance_officer_home, name='compliance_officer_home'),
    path('car_store_manager/', views.car_store_manager_home, name='car_store_manager_home'),
    path('coffee_store_manager/', views.coffee_store_manager_home, name='coffee_store_manager_home'),
    # path('accounts/login/', views.login_user, name='login1'),
    # path('accounts/', include('django.contrib.auth.urls'),name='login1'),
]
