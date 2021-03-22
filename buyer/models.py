import uuid

from django.conf import settings
from django.db import models


class Buyer(models.Model):
    buyer_user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    buyer_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    buyer_address = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Buyer: buyer_id{str(self.buyer_id)} buyer_address:{self.buyer_address}"
