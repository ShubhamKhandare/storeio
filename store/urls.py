from django.urls import path

from store.views import StoreListCreateView, StoreRetrieveView

urlpatterns = [
    path('', StoreListCreateView.as_view()),
    path('<pk>', StoreRetrieveView.as_view())
]
