from django.urls import path

from store.views import StoreListCreateView

urlpatterns = [
    path('', StoreListCreateView.as_view())
]
