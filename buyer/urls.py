from django.urls import path

from buyer.views import OrderCreateView, ProductCatalogListView, ProductByCategoryListView, CartCreateView, \
    CartRetrieveUpdateView, CartToOrderCreateView

urlpatterns = [
    path('order/', OrderCreateView.as_view()),
    path('store/<store_id>/catalog', ProductCatalogListView.as_view()),
    path('store/<store_id>/<category_type>', ProductByCategoryListView.as_view()),
    path('cart/', CartCreateView.as_view()),
    path('cart/<cart_id>', CartRetrieveUpdateView.as_view()),
    path('cart/<cart_id>/order', CartToOrderCreateView.as_view())
]
