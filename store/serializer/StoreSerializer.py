from rest_framework import serializers

from seller.serializer.SellerSerializer import UserSerializer
from store.models import Store


class StoreListCreateSerializer(serializers.ModelSerializer):
    store_link = serializers.CharField(read_only=True)
    seller = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Store
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['seller'] = UserSerializer(instance.seller).data
        return response
