# Create your views here.
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from buyer.models import Buyer
from buyer.serializer.BuyerSerializer import BuyerListCreateSerializer
from buyer.serializer.BuyerTokenSerializer import BuyerAccessTokenSerializer


class BuyerAPIView(ListCreateAPIView):
    # TODO add logging
    # permission_classes = (IsAuthenticated,)
    queryset = Buyer.objects.all()
    serializer_class = BuyerListCreateSerializer


class BuyerTokenObtainPairView(TokenObtainPairView):
    serializer_class = BuyerAccessTokenSerializer
