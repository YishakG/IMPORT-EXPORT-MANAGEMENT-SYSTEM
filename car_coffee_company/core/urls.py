from django.urls import path
from . import views
urlpatterns = [
    path('about/', views.about_view, name="SIEMS_about"),
    path('', views.home , name="SIEMS_home"),

]

