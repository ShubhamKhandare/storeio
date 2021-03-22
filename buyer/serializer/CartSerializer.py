from rest_framework import serializers

from buyer.models import Cart


class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
