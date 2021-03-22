import urllib

from django.conf import settings
from django.db import IntegrityError
from rest_framework import status
from rest_framework.exceptions import APIException, PermissionDenied
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, get_object_or_404, ListAPIView, \
    RetrieveUpdateAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from buyer.models import Order
from store.models import Store, Product
from store.serializer.ProductSerializer import ProductListCreateSerializer
from store.serializer.StoreOrderSerializer import StoreOrderListSerializer, StoreOrderUpdateSerializer
from store.serializer.StoreSerializer import StoreListCreateSerializer


class StoreListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StoreListCreateSerializer

    def get_queryset(self):
        # Only list objects where you are
        queryset = Store.objects.filter(seller=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            store_link = settings.DOMAIN_NAME + urllib.parse.quote_plus(str(serializer.validated_data['store_name']))
            try:
                serializer.save(seller=request.user, store_link=store_link)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as exc:
                raise APIException(exc)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreRetrieveView(RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListCreateSerializer


class ProductListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductListCreateSerializer
    parser_class = (FileUploadParser,)

    def get_queryset(self):
        store_id = self.kwargs.get('store_id')
        return Product.objects.filter(store=store_id)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # TODO check correct user adding product
            store_id = kwargs.get('store_id')
            store_obj = get_object_or_404(Store, store_id=store_id)
            try:
                serializer.save(store=store_obj)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as exc:
                raise APIException(exc)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreOrderListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StoreOrderListSerializer

    def get_queryset(self):
        store_id = self.kwargs.get('store_id')
        store_obj = get_object_or_404(Store, store_id=store_id)
        if store_obj.seller != self.request.user:
            # Only Store owner can see the orders
            raise PermissionDenied()
        return Order.objects.filter(product__store=store_obj)


class StoreOrderGetUpdateView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StoreOrderUpdateSerializer
    lookup_field = 'order_id'

    def get_queryset(self):
        store_id = self.kwargs.get('store_id')
        store_obj = get_object_or_404(Store, store_id=store_id)
        if store_obj.seller != self.request.user:
            # Only Store owner can see the orders
            raise PermissionDenied()
        return Order.objects.filter(product__store=store_obj)
