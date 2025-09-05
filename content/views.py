from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category
# Create your views here.

def home(request):
    return HttpResponse("Welcome to My Company")

def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})

def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(categories=category)

    return render(
            request,
            "products_by_category.html",
            {"category": category, "products": products}
            )

def product_range(request, min_price, max_price):
    products = Product.objects.filter(price__gte=min_price, price__lte=max_price)

    return render(
        request,
        "products_range.html",
        {
            "min_price": min_price,
            "max_price": max_price,
            "products": products
            }


            )
