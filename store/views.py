import urllib

from django.conf import settings
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from store.models import Store
from store.serializer.StoreSerializer import StoreListCreateSerializer


class StoreListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StoreListCreateSerializer
    queryset = Store.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            store_link = settings.DOMAIN_NAME + urllib.parse.quote_plus(str(serializer.validated_data['store_name']))
            serializer.save(seller=request.user, store_link=store_link)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreRetrieveView(RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListCreateSerializer
