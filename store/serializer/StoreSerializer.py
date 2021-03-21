from rest_framework import serializers

from seller.serializer.SellerSerializer import UserSerializer
from store.models import Store


class StoreListCreateSerializer(serializers.ModelSerializer):
    store_link = serializers.SerializerMethodField()
    seller = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Store
        fields = '__all__'

    def create(self, **kwargs):
        kwargs["seller"] = self.fields["seller"].get_default()
        return super().create(**kwargs)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['seller'] = UserSerializer(instance.seller).data
        return response
