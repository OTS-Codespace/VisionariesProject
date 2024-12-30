from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    # model fields here
    pass

class OrderStatus(models.TextChoices):
    """
    Enum-like class for order status choices.
    """
    PENDING = 'Pending', 'Pending'
    PROCESSING = 'Processing', 'Processing'
    SHIPPED = 'Shipped', 'Shipped'
    DELIVERED = 'Delivered', 'Delivered'
    CANCELLED = 'Cancelled', 'Cancelled'


class Order(models.Model):
    """
    Represents a customer order.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )
    payment_status = models.CharField(
        max_length=20,
        choices=[
            ('Paid', 'Paid'),
            ('Pending', 'Pending'),
            ('Failed', 'Failed')
        ],
        default='Pending'
    )
    shipping_address = models.TextField(null=True, blank=True)
    shipping_method = models.CharField(max_length=50, null=True, blank=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_total(self):
        """
        Calculate the total order price, including tax.
        """
        subtotal = sum(item.total_price for item in self.items.all())
        return subtotal + self.tax

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"


class OrderItem(models.Model):
    """
    Represents an item in an order.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('Product', on_delete=models.PROTECT)  # Replace 'Product' with your product model
    quantity = models.PositiveIntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        """
        Override save to update inventory and calculate total price.
        """
        if not self.pk:  # New item
            self.product.stock -= self.quantity  # Update inventory
            self.product.save()
        self.total_price = self.price_per_item * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"


class OrderStatusHistory(models.Model):
    """
    History of status changes for an order.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='status_history')
    previous_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.order.id} status changed to {self.new_status}"
