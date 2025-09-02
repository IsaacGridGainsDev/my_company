from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def home(request):
    return HttpResponse("Welcome to My Company")

def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})
