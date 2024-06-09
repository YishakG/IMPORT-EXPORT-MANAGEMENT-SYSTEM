from django.shortcuts import render
from django.http import HttpResponse

def home(response):
    return render(response,'core/home.html')

def about_view(response):
    return render(response,'core/about.html')

