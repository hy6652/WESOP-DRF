from django.urls import path
from .views import CartDetailView, CartListView


urlpatterns = [
    path('/<int:pk>', CartDetailView.as_view()),
    path('', CartListView.as_view()),
]