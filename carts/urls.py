from django.urls import path
from .views import CartListGV, CartDetailView, CartListView


urlpatterns = [
    # path('', CartView.as_view()),
    # path('/cart/<int:cart_id>', CartView.as_view()),
    # path('/<int:pk>', CartListGV.as_view()),
    # path('/create/<int:pk>', CartCreateView.as_view()),
    path('/<int:pk>', CartDetailView.as_view()),
    path('', CartListView.as_view()),
]