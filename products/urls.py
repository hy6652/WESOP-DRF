from  django.urls import path

from products.views import (CategoryListGV, CategoryDetailGV,ProductDetailGV, ProductListGV,
                            ReviewListGV, ReviewCreateGV, ReviewDetailGV)

urlpatterns = [
    path('/categories/<int:pk>', CategoryDetailGV.as_view(), name='category-detail'),
    path('/categories', CategoryListGV.as_view(), name='category-list'),
    path('', ProductListGV.as_view(), name='product-list'),
    path('/<int:pk>' , ProductDetailGV.as_view(), name='product-detail'),
    path('/<int:pk>/reviews' , ReviewListGV.as_view(), name='review-list'),
    path('/review/<int:pk>' , ReviewDetailGV.as_view(), name='review-detail'),
    path('/<int:pk>/review-create' , ReviewCreateGV.as_view(), name='review-create'),
]