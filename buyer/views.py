from django.db import IntegrityError
from django.db.models import Count
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from buyer.serializer.CatalogSerializer import CatalogListSerializer
from buyer.serializer.OrderSerializer import OrderCreateSerializer
from store.models import Category, Product


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
        product_qs = Product.objects.filter(store=store_id)
        products_list = product_qs.values_list('product_category_id', flat=True)
        category_qs = Category.objects.filter(type__in=products_list, products__in=product_qs)
        return category_qs.values('type').annotate(count=Count('products')).order_by('-count')
