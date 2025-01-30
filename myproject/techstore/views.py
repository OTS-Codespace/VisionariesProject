from argparse import Action
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem
from .forms import CustomerRegistrationForm, CheckoutForm
from decimal import Decimal


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




class CheckOutView(View):
    def post(self, request):
        # Get the user's pending order
        try:
            order = Order.objects.get(customer=request.user, status='Pending')
        except Order.DoesNotExist:
            return redirect("product_list")  # Redirect if no order exists

        # Get selected product IDs from the form
        selected_product_ids = request.POST.getlist('selected_products')

        # Filter only selected items
        order_items = order.items.filter(id__in=selected_product_ids)

        # Calculate total price based on selected products
        total_price = sum(item.get_total_price() for item in order_items) if order_items else Decimal('0.00')
        
        # Define shipping cost and tax rate
        shipping_cost = Decimal('4.99') if order_items else Decimal('0.00')
        tax_rate = Decimal('0.10')  # 10% tax
        tax = total_price * tax_rate
        final_total = total_price + shipping_cost + tax

        # Context for the template
        context = {
            'order_items': order.items.all(),  # Show all items for selection
            'selected_items': order_items,  # Show selected items in order summary
            'order_summary': {
                'total_price': total_price,
                'shipping_cost': shipping_cost,
                'tax': tax,
                'final_total': final_total,
                'tax_rate': tax_rate,
            },
        }
        return render(request, 'amazon/checkout.html', context)

    def get(self, request):
        try:
            order = Order.objects.get(customer=request.user, status='Pending')
        except Order.DoesNotExist:
            order = None

        context = {
            'order_items': order.items.all() if order else [],
            'selected_items': [],
            'order_summary': {
                'total_price': Decimal('0.00'),
                'shipping_cost': Decimal('0.00'),
                'tax': Decimal('0.00'),
                'final_total': Decimal('0.00'),
                'tax_rate': Decimal('0.10'),
            },
        }
        return render(request, 'amazon/checkout.html', context)




class RemoveFromCartView(View):
    def get(self, request, item_id):
        # Get the order item and delete it
        order_item = get_object_or_404(OrderItem, id=item_id)

        # Ensure the user is authorized to remove the item (belongs to their order)
        if order_item.order.customer == request.user:
            order_item.delete()

        return redirect('checkout')  # Redirect back to checkout after removing




class OrdersView(View):
    def get(self, request):
        return render(request, 'amazon/orders.html')
    
class TrackingView(View):
    def get(self, request):
        return render(request, 'amazon/tracking.html')


class ProductDetailView(View):
    def get(self, request, id): 
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return redirect('404')

        context = {
            "product": product,
        }

        return render(request, 'amazon/product_detail.html', context)



class AddToCartView(View):
    def post(self, request, product_id):
        # Get the product object based on the product_id
        product = get_object_or_404(Product, id=product_id)

        # Get or create the user's pending order
        order, created = Order.objects.get_or_create(
            customer=request.user, status='Pending'
        )

        # Get or create the order item for the product
        order_item, item_created = OrderItem.objects.get_or_create(
            order=order, product=product,
            defaults={'price': product.price, 'quantity': 1}  # Initial quantity set to 1
        )

        # If the item already exists in the cart, increase the quantity
        if not item_created:
            order_item.quantity += 1
            order_item.save()

        # Get action from form data
        action = request.POST.get('action', 'add_to_cart')  # Fix variable name

        # If action is "buy_now", redirect to checkout, otherwise stay on the product page
        if action == "buy_now":
            return redirect('checkout')  # Redirect to checkout page
        else:
            return redirect(request.META.get('HTTP_REFERER', '/'))  # Stay on the same page




# class RatingStars(View):
#     def get(self, request):
#         products = Product.objects.all()   
    


# def register(request):
#     if request.method == 'POST':
#         form = CustomerRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('product_list')  # Redirect to dashboard after registration
#     else:
#         form = CustomerRegistrationForm()
#     return render(request, 'amazon/register.html', {'form': form})


def dashboard(request):
    user = request.user
    orders = user.orders.all()  # Assuming a related Order model
    wishlist = user.wishlist.all()  # Assuming a related Wishlist model
    return render(request, 'amazon/dashboard.html', {'user': user, 'orders': orders, 'wishlist': wishlist})




    