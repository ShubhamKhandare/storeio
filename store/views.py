from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from store.models import Store
from store.serializer.StoreSerializer import StoreListCreateSerializer


class StoreListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StoreListCreateSerializer
    queryset = Store.objects.all()


class StoreRetrieveView(RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListCreateSerializer
