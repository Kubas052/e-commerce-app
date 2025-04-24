from django.contrib import admin

# Register your models here.

from .models import Product, Category, Customer, Order, OrderItem, ShippingAddress

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Category)