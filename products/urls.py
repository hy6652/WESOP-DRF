from  django.urls import path
from products.views import (RecommendedView, CategoryListGV, CategoryDetailGV,
                            ProductReviewView, ProductDetailGV, ProductListGV)

urlpatterns = [
    # path('/categories', CategoryListView.as_view()),
    # path('/categories/<int:category_id>', CategoryDetailView.as_view()),
    path('/recommend/<int:product_id>' , RecommendedView.as_view()),

    path('/categories/<int:pk>', CategoryDetailGV.as_view()),
    path('/categories', CategoryListGV.as_view()),
    path('', ProductListGV.as_view()),
    path('/<int:pk>' , ProductDetailGV.as_view(), name='product-detail'),

    path('/review' , ProductReviewView.as_view()),
    path('/review/<int:review_id>' , ProductReviewView.as_view())
]