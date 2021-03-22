from rest_framework import serializers

from seller.models import Seller


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['seller_id', 'mobile_number']
