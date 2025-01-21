from django.shortcuts import render
from .models import Product
from django.views.generic import View
# Create your views here.


class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'amazon/index.html', {'products': products})
    
class CheckOutView(View):
    def get(self, request):
        return render(request, 'amazon/checkout.html')
    
class OrdersView(View):
    def get(self, request):
        return render(request, 'amazon/orders.html')
    
class TrackingView(View):
    def get(self, request):
        return render(request, 'amazon/tracking.html')