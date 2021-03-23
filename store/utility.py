from django_filters.rest_framework import FilterSet

from buyer.models import Order


class OrderListFilter(FilterSet):
    class Meta:
        model = Order
        fields = ['status']
