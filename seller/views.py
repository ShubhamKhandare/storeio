from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from seller.models import Seller
from seller.serializer import SellerSerializer, SellerTokenObtainPairSerializer


class SellerAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer.UserSerializer


class SellerTokenObtainPairView(TokenObtainPairView):
    serializer_class = SellerTokenObtainPairSerializer.SellerAccessTokenSerializer


# class SellerTokenRefreshView(TokenRefreshView):
#     serializer_class = SellerTokenRefreshSerializer.

class SellerSelfUpdateView(UpdateAPIView):
    serializer_class = SellerSerializer.UserUpdateSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        return Seller.objects.filter(pk=self.request.user.pk)

    def get_object(self):
        self.check_object_permissions(self.request, self.request.user)
        return self.request.user
