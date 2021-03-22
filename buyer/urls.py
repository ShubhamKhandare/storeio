from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from buyer.views import BuyerAPIView, BuyerTokenObtainPairView

urlpatterns = [
    path('', BuyerAPIView.as_view()),
    path('api/token', BuyerTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
]
