import logging

from django.conf import settings
from rest_framework import serializers

from seller.serializer.SellerSerializer import UserSerializer
from store.models import Store


class StoreListCreateSerializer(serializers.ModelSerializer):
    store_link = serializers.SerializerMethodField()
    seller = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Store
        fields = '__all__'

    def get_store_link(self, obj):
        # This is store link getter
        # TODO encode url properly
        store_link = settings.DOMAIN_NAME + obj.store_name
        logging.info(f"Created store link f{store_link}")
        return store_link

    def save(self, **kwargs):
        kwargs["seller"] = self.fields["seller"].get_default()
        return super().save(**kwargs)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['seller'] = UserSerializer(instance.seller).data
        return response
