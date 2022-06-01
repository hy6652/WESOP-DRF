from  django.urls import path
from products.views import (ProductListView, RecommendedView,
                            CategoryListView, CategoryDetailView, ProductReviewView,
                            ProductDetailGV)

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/categories', CategoryListView.as_view()),
    path('/categories/<int:category_id>', CategoryDetailView.as_view()),
    path('/recommend/<int:product_id>' , RecommendedView.as_view()),

    path('/<int:pk>' , ProductDetailGV.as_view(), name='product-detail'),

    path('/review' , ProductReviewView.as_view()),
    path('/review/<int:review_id>' , ProductReviewView.as_view())
]