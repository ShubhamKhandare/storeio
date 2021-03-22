import uuid

from django.db import models

from seller.models import Seller
from store.models import Product


class Order(models.Model):
    class OrderType(models.TextChoices):
        SUBMITTED = 'Submitted'
        ACCEPTED = 'Accepted'
        COMPLETED = 'Completed'
        DECLINED = 'Declined'

    order_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    status = models.CharField(
        max_length=20,
        choices=OrderType.choices,
        default=OrderType.SUBMITTED,
    )
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    buyer = models.ForeignKey(Seller, related_name='orders', on_delete=models.CASCADE, )
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order: order_id:{self.order_id} product: {self.product} buyer: {self.buyer}"

    class Meta:
        ordering = ['-updated_at']
        unique_together = ('product', 'buyer')


class Cart(models.Model):
    cart_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    product = models.ManyToManyField(Product)
    buyer = models.ForeignKey(Seller, related_name='carts', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart: cart_id:{self.cart_id} product: {self.product} buyer:{self.buyer}"

    class Meta:
        ordering = ['-updated_at']
