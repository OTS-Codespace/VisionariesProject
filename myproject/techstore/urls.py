from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
<<<<<<< HEAD
from .views import ProductListView, ProductDetailView, CheckOutView, OrdersView, TrackingView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
=======
<<<<<<< Updated upstream
from .views import ProductListView,CheckOutView,OrdersView,TrackingView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
=======
from .views import ProductListView, ProductDetailView, CheckOutView, OrdersView, TrackingView, AddToCartView, RemoveFromCartView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
>>>>>>> Stashed changes
>>>>>>> Jeff
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    path('checkout/<int:id>/', views.CheckOutView.as_view(), name='checkout'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('tracking/', TrackingView.as_view(), name='tracking'),
    path('remove_from_cart/<int:item_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('add_to_cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('add_to_cart/<int:product_id>/buy_now/', AddToCartView.as_view(), name='buy_now'),  # Buy Now
    # path('cart/', views.cart_view, name='cart'),
    # path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('login/', auth_views.LoginView.as_view(template_name='amazon/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('register/', views.register, name='register'),
    # path('dashboard/', views.dashboard, name='dashboard'),
]



