from django.contrib import admin

from .models import Product, Category, Customer, Order, OrderItem, Payment, Shipping, Customer

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Shipping)




# from django.contrib import admin
# from .models import Product, Order, OrderItem

# admin.site.register(Product)
# admin.site.register(Order)
# admin.site.register(OrderItem)
admin.site.register(Customer)

