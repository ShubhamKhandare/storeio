from django.urls import path

from seller.views import SellerAPIView

urlpatterns = [
    path('', SellerAPIView.as_view()),
]
