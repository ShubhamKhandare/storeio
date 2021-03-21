import logging

from django.db import transaction
from rest_framework import serializers

from store.models import Product, Category
from store.serializer.CategorySerializer import CategoryCreateListSerializer


class ProductListCreateSerializer(serializers.ModelSerializer):
    store = serializers.PrimaryKeyRelatedField(read_only=True)
    product_category = CategoryCreateListSerializer()

    def create(self, validated_data):
        with transaction.atomic():
            category_data = validated_data.pop('product_category')
            category_obj, created = Category.objects.get_or_create(**category_data)
            if created:
                logging.info(f"Created new category: {category_obj}")
            product_obj = Product.objects.create(**validated_data, product_category=category_obj)
            return product_obj

    class Meta:
        model = Product
        fields = '__all__'

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['seller'] = UserSerializer(instance.seller).data
    #     return response
