from django.urls import path

from store.views import StoreListCreateView, StoreRetrieveView, ProductListCreateView, StoreOrderListView, \
    StoreOrderGetUpdateView

urlpatterns = [
    path('', StoreListCreateView.as_view()),
    path('<pk>', StoreRetrieveView.as_view()),
    path('<store_id>/product', ProductListCreateView.as_view()),
    path('<store_id>/order', StoreOrderListView.as_view()),
    path('<store_id>/order/<order_id>', StoreOrderGetUpdateView.as_view()),
]
