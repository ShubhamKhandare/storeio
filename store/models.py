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
