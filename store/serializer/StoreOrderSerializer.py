from rest_framework import serializers

from buyer.models import Order


class StoreOrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class StoreOrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
