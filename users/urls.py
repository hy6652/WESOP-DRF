from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from users.views import RegistrationAPIView

urlpatterns = [
    path('/register', RegistrationAPIView.as_view(), name='register'),
    path('/login', obtain_auth_token, name='login')
]