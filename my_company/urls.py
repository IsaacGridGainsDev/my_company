"""
URL configuration for my_company project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from content import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.product_list, name='product_list'),
    path("products/category/<int:category_id>/", views.products_by_category, name="products_by_category"),
    path("products/range/<int:min_price>-<int:max_price>/", views.products_range, name="products_range"),
    path("products-cbv/", ProductListView.as_view(), name="product_list_cbv"),
    path("product/<int>:pk>/", ProductDetailView.as_view(), name="product_detail_cbv"),
    path("products/range-cbv/<int:min_price>-<int:max_price>/", ProductRangeView.as_view(), name="product_range_cbv")
]
