from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from seller.views import SellerAPIView, SellerTokenObtainPairView

urlpatterns = [
    path('', SellerAPIView.as_view()),
    # TODO add endpoint to send the actual OTP
    path('api/token', SellerTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
]
