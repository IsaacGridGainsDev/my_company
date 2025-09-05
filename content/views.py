from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
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
class ProductListView(ListView):
    model = Product
    template_name = "product_list_cbv.html"
    context_objecy_name = "products"

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail_cbv.html"
    context_object_name = "product"

class ProductRangeView(ListView):
    model = Product
    template_name = "products_range_cbv.html"
    context_object_name = "products"

    def get_queryset(self):
        min_price = self.kwargs["min_price"]
        max_price = self.kwargs["max_price"]
        return Product.objects.filter(price__gte=min_price, price_lte=max_price)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["min_price"] = self.kwargs["min_price"]
        context["max_price"]=self.kwargs["max_price"]
        return context
