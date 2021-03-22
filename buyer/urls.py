from django.urls import path

from buyer.views import OrderCreateView, ProductCatalogListView, ProductByCategoryListView

urlpatterns = [
    path('order/', OrderCreateView.as_view()),
    path('store/<store_id>/catalog', ProductCatalogListView.as_view()),
    path('store/<store_id>/<category_type>', ProductByCategoryListView.as_view())
]
