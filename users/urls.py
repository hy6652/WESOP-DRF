from django.urls import path

# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import RegistrationAPIView

urlpatterns = [
    path('/register', RegistrationAPIView.as_view(), name='register'),
    # path('/login', obtain_auth_token, name='login'),
    path('/api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]