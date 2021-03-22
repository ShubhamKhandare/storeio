from django.urls import path

from buyer.views import OrderCreateView, ProductCatalogListView

urlpatterns = [
    path('order/', OrderCreateView.as_view()),
    path('store/<store_id>/catalog', ProductCatalogListView.as_view())
]
