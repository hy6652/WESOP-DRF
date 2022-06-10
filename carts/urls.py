from django.urls import path
from .views import CartDetailView, CartListView


urlpatterns = [
    path('/<int:pk>', CartDetailView.as_view(), name='cart-detail'),
    path('', CartListView.as_view(), name='cart-list'),
]