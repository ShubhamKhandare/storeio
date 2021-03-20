from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from seller.models import Seller
from seller.serializer import SellerSerializer, SellerTokenObtainPairSerializer


class SellerAPIView(ListAPIView):
    # TODO add logging
    permission_classes = (IsAuthenticated,)
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer.UserSerializer


class SellerTokenObtainPairView(TokenObtainPairView):
    serializer_class = SellerTokenObtainPairSerializer.SellerAccessTokenSerializer

# TODO check if any needs to be done for refresh token
# class SellerTokenRefreshView(TokenRefreshView):
#     serializer_class = SellerTokenRefreshSerializer.
