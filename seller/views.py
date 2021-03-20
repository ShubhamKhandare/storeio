from rest_framework.generics import ListCreateAPIView

from seller.models import Seller
from seller.serializer import SellerSerializer


class SellerAPIView(ListCreateAPIView):
    # TODO add logging
    # permission_classes = (IsAuthenticated,)
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer.UserSerializer
