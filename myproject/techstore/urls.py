from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ProductListView,CheckOutView,OrdersView,TrackingView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('tracking/', TrackingView.as_view(), name='tracking'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('login/', auth_views.LoginView.as_view(template_name='amazon/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
