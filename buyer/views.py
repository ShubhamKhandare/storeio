from django.db import IntegrityError
from django.db.models import Count
from rest_framework import status
from rest_framework.exceptions import APIException, PermissionDenied
from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from buyer.models import Cart
from buyer.serializer.CartSerializer import CartCreateSerializer, CartRetrieveUpdateSerializer
from buyer.serializer.CatalogSerializer import CatalogListSerializer, ProductByCategoryListSerializer
from buyer.serializer.OrderSerializer import OrderCreateSerializer, CartToOrderCreateSerializer
from store.models import Category, Product, Store


class OrderCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                requested_buyer = request.user
                serializer.save(buyer=requested_buyer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as exc:
                raise APIException(exc)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductCatalogListView(ListAPIView):
    serializer_class = CatalogListSerializer

    def get_queryset(self):
        store_id = self.kwargs.get('store_id')
        store_obj = get_object_or_404(Store, store_id=store_id)
        product_qs = Product.objects.filter(store=store_obj)
        products_list = product_qs.values_list('product_category_id', flat=True)
        category_qs = Category.objects.filter(type__in=products_list, products__in=product_qs)
        return category_qs.values('type').annotate(count=Count('products')).order_by('-count')


class ProductByCategoryListView(ListAPIView):
    serializer_class = ProductByCategoryListSerializer

    def get_queryset(self):
        store_id = self.kwargs.get('store_id')
        store_obj = get_object_or_404(Store, store_id=store_id)
        category_type = self.kwargs.get('category_type')
        product_qs = Product.objects.filter(store=store_obj, product_category__type=category_type)
        return product_qs


class CartCreateView(CreateAPIView):
    serializer_class = CartCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                if request.user.is_authenticated:
                    requested_buyer = request.user
                    serializer.save(buyer=requested_buyer)
                else:
                    serializer.save(buyer=None)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as exc:
                raise APIException(exc)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = CartRetrieveUpdateSerializer
    lookup_field = 'cart_id'

    def get_queryset(self):
        queryset = Cart.objects.all()
        return queryset

    def perform_update(self, serializer):
        instance = serializer.save()
        buyer_obj = instance.buyer
        if buyer_obj and buyer_obj != self.request.user:
            # if Cart created by registered buyer then only buyer can update
            raise PermissionDenied()


class CartToOrderCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CartToOrderCreateSerializer

    def create(self, request, *args, **kwargs):
        cart_id = kwargs.get('cart_id')
        cart_obj = get_object_or_404(Cart, cart_id=cart_id)
        cart_dict = CartCreateSerializer(cart_obj).data
        request_data = request.data
        request_data.update(cart_dict)
        serializer = self.serializer_class(data=request_data)
        if serializer.is_valid():
            try:
                requested_buyer = request.user
                serializer.save(buyer=requested_buyer)
                # Deleting cart as cart is successfully converted to order
                cart_obj.delete()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as exc:
                raise APIException(exc)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
