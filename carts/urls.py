from django.urls import path
from .views import CartView, CartListGV


urlpatterns = [
    # path('', CartView.as_view()),
    # path('/cart/<int:cart_id>', CartView.as_view()),
    path('/<int:pk>', CartListGV.as_view()),
]