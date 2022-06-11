import json
from django.forms import ValidationError

from rest_framework             import generics
from rest_framework             import filters
from rest_framework.response    import Response
from rest_framework.permissions import IsAuthenticated

from django.http      import JsonResponse
from django.views     import View
from django.http      import JsonResponse
# from django.db.models import Q

from cores.utils          import author
from products.pagination  import CategoryLimitOffsetPagination
from products.serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from products.models      import Category, Product, Ingredient, SkinType, ProductFeelings, Review


class ProductListGV(generics.ListAPIView):
    queryset         = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends  = [filters.SearchFilter]
    search_fields    = ['^name', '=category__id', '^skin_type__name', 'feeling__name', '^ingredient__name']


class ProductDetailGV(generics.RetrieveAPIView):
    queryset         = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListGV(generics.ListAPIView):
    queryset         = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryLimitOffsetPagination


class CategoryDetailGV(generics.RetrieveAPIView):
    queryset         = Category.objects.all()
    serializer_class = CategorySerializer


class ReviewListGV(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Review.objects.filter(product=pk)


class ReviewDetailGV(generics.RetrieveAPIView):
    queryset         = Review.objects.all()
    serializer_class = ReviewSerializer

 
class ReviewCreateGV(generics.CreateAPIView):
    serializer_class   = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pk      = self.kwargs.get('pk')
        user    = self.request.user
        product = Product.objects.get(pk=pk)

        if Review.objects.filter(product=product, user=user).exists():
            raise ValidationError("your review for this product already exists")
        serializer.save(product=product, user=user)