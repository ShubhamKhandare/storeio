from rest_framework import serializers

from store.models import Category


class CatalogListSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
