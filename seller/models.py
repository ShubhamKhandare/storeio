import uuid as uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class SellerManager(BaseUserManager):
    def create_user(self, mobile_number):
        """
        Creates seller with phone number
        """
        if not mobile_number:
            raise ValueError('Seller must have a phone number')

        user = self.model(
            mobile_number=mobile_number
        )

        # As authentication is done from mobile number OTP
        # https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#django.contrib.auth.models.User.set_unusable_password
        user.set_unusable_password()
        user.save(using=self._db)
        return user


# Create your models here.
class Seller(AbstractBaseUser):
    seller_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    # TODO add phone number validations
    mobile_number = models.BigIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = SellerManager()
    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = ['mobile_number']

    class Meta:
        ordering = ['seller_id']

    def __str__(self):
        return f"Seller: ID:{self.seller_id} mobile_number:{self.mobile_number}"
