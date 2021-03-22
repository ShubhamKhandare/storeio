from rest_framework import serializers

from seller.models import Seller


class UserSerializer(serializers.ModelSerializer):
    seller_user = serializers.PrimaryKeyRelatedField(read_only=True, )

    def get_cleaned_data(self):
        data = super(UserSerializer, self).get_cleaned_data()
        return data

    def save(self, request):
        user = super(UserSerializer, self).save(request)
        user.is_seller = True
        user.save()
        seller = Seller(seller_user=user)
        seller.save()
        return user

    class Meta:
        model = Seller
        fields = ['seller_id', 'mobile_number']
