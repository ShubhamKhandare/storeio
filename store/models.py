import uuid

from django.db import models

from seller.models import Seller


class Store(models.Model):
    store_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    seller = models.ForeignKey(Seller, related_name='stores', on_delete=models.CASCADE, )
    store_name = models.TextField(unique=True, max_length=90)
    store_address = models.TextField(max_length=255)
    store_link = models.TextField(max_length=255)

    def __str__(self):
        return f"Store: store_id:{self.store_id} store_name:{self.store_name}"

    class Meta:
        ordering = ['store_id']


class Category(models.Model):
    type = models.TextField(max_length=90, primary_key=True)

    def __str__(self):
        return f"Category: type {self.type}"

    class Meta:
        ordering = ['type']


class Product(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    store = models.ForeignKey(Store, related_name='products', on_delete=models.CASCADE)
    product_name = models.TextField(max_length=90)
    product_description = models.TextField(max_length=255)
    product_mrp = models.IntegerField()
    product_sale_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # If category is not present in request or gets deleted this will be set to type misc
    product_category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_DEFAULT,
                                         default='misc')

    # product_image =

    def __str__(self):
        return f"Product: product_id:{self.product_id} store_name:{self.store} name:{self.product_name}"

    class Meta:
        ordering = ['product_name']
        unique_together = ('store', 'product_name',)
