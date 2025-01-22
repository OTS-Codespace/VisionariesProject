from django.shortcuts import render
from .models import Product
from django.views.generic import View
from django.contrib.auth import login
from .forms import CustomerRegistrationForm
from django.contrib.auth.decorators import login_required
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
    
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomerRegistrationForm

def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')  # Redirect to dashboard after registration
    else:
        form = CustomerRegistrationForm()
    return render(request, 'amazon/register.html', {'form': form})

# @login_required
def dashboard(request):
    user = request.user
    orders = user.orders.all()  # Assuming a related Order model
    wishlist = user.wishlist.all()  # Assuming a related Wishlist model
    return render(request, 'amazon/dashboard.html', {'user': user, 'orders': orders, 'wishlist': wishlist})

