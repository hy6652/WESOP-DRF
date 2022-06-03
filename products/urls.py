from  django.urls import path

from products.views import (RecommendedView, CategoryListGV, CategoryDetailGV,
                            ProductDetailGV, ProductListGV,
                            ReviewListGV, ReviewCreateGV, ReviewDetailGV)

urlpatterns = [
    # path('/categories', CategoryListView.as_view()),
    # path('/categories/<int:category_id>', CategoryDetailView.as_view()),
    path('/recommend/<int:product_id>' , RecommendedView.as_view()),

    path('/categories/<int:pk>', CategoryDetailGV.as_view()),
    path('/categories', CategoryListGV.as_view()),
    path('', ProductListGV.as_view()),
    path('/<int:pk>' , ProductDetailGV.as_view(), name='product-detail'),

    path('/<int:pk>/reviews' , ReviewListGV.as_view()),
    path('/review/<int:pk>' , ReviewDetailGV.as_view()),
    path('/<int:pk>/review-create' , ReviewCreateGV.as_view()),

    # path('/<int:product_id>/review' , ProductReviewView.as_view()),
    # path('/review/<int:review_id>' , ProductReviewView.as_view())
]