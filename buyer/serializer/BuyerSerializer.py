from rest_framework import serializers

from buyer.models import Buyer


class BuyerListCreateSerializer(serializers.ModelSerializer):
    buyer_user = serializers.PrimaryKeyRelatedField(read_only=True, )

    def get_cleaned_data(self):
        data = super(BuyerListCreateSerializer, self).get_cleaned_data()
        extra_data = {
            'buyer_address': self.validated_data.get('buyer_address', ''),
        }
        data.update(extra_data)
        return data

    def save(self):
        import pdb
        pdb.set_trace()
        user = super(BuyerListCreateSerializer, self).save()
        user.is_buyer = True
        user.save()
        buyer_obj = Buyer(buyer_user=user, buyer_address=self.cleaned_data.get('buyer_address'))
        buyer_obj.save()
        return user

    class Meta:
        model = Buyer
        fields = ['buyer_id', 'buyer_address', 'buyer_user']
