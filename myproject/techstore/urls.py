from django.urls import path
from . import views
from .views import ProductListView,CheckOutView,OrdersView,TrackingView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('tracking/', TrackingView.as_view(), name='tracking'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
