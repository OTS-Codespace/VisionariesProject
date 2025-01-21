from django.urls import path
from . import views
from .views import ProductListView,CheckOutView,OrdersView,TrackingView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('tracking/', TrackingView.as_view(), name='tracking'),
]
