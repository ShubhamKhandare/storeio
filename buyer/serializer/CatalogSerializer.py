from rest_framework import serializers

from store.models import Category, Product


class CatalogListSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class ProductByCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
