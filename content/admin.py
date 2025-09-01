from django.contrib import admin
from .models import Employee, Department, Product, ProdDesc

# Register your models here.

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Product)
admin.site.register(ProdDesc)
