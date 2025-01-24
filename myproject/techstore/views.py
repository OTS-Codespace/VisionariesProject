from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem
from .forms import CustomerRegistrationForm, CheckoutForm

# Create your views here.



class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        for product in products:
            product.rating_stars = int(product.rating * 10)  # Pre-calculate rating stars
        return render(request, 'amazon/index.html', {'products': products})

class CheckOutView(View):
    def get(self, request):
        return render(request, 'amazon/checkout.html')
    
    def post(self, request):
        # Handle the form submission here
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            return redirect('orders')
        return render(request, 'amazon/checkout.html', {'form': form})

class OrdersView(View):
    def get(self, request):
        return render(request, 'amazon/orders.html')
    
class TrackingView(View):
    def get(self, request):
        return render(request, 'amazon/tracking.html')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'amazon/product_detail.html'
    context_object_name = 'product'
    
# class RatingStars(View):
#     def get(self, request):
#         products = Product.objects.all()   
    


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

@login_required
def dashboard(request):
    user = request.user
    orders = user.orders.all()  # Assuming a related Order model
    wishlist = user.wishlist.all()  # Assuming a related Wishlist model
    return render(request, 'amazon/dashboard.html', {'user': user, 'orders': orders, 'wishlist': wishlist})

def cart_initialize(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}

def cart_count(cart):
    return sum(item['quantity'] for item in cart.values())

def cart_view(request):
    cart_initialize(request)
    cart = request.session['cart']
    cart_items = []
    total_price = 0
    total_quantity = cart_count(cart)

    if not cart:
        message = "Your cart is empty. Add items to your cart."
    else:
        message = None

    for product_id, details in cart.items():
        product = get_object_or_404(Product, id=product_id)
        quantity = details['quantity']
        total_price += product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': product.price * quantity
        })

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_quantity': total_quantity,
        'message': message
    }
    return render(request, 'store/cart.html', context)

def add_to_cart(request, product_id):
    cart_initialize(request)
    product = get_object_or_404(Product, id=product_id)
    cart = request.session['cart']

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {'quantity': 1}

    request.session.modified = True
    total_quantity = cart_count(cart)
    return JsonResponse({'total_quantity': total_quantity})  # For AJAX updates

def remove_from_cart(request, product_id):
    cart_initialize(request)
    cart = request.session['cart']

    if str(product_id) in cart:
        if cart[str(product_id)]['quantity'] > 1:
            cart[str(product_id)]['quantity'] -= 1
        else:
            del cart[str(product_id)]

    request.session.modified = True
    total_quantity = cart_count(cart)
    return JsonResponse({'total_quantity': total_quantity})  # For AJAX updates




