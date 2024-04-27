from django.shortcuts import render
from . import views

# Create your views here.

def stockPicker(request):
    return render(request, 'stock_main/stockpicker.html') 

def stockTracker(request):
    return render(request, 'stock_main/stocktracker.html') 