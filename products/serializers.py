from rest_framework import serializers

from products.models import (Category, Product, ProductFeelings,
                            ProductIngredient, ProductSkintype)


class ProductFeelingsSerializer(serializers.ModelSerializer):
    feeling = serializers.CharField(source='name')

    class Meta:
        model  = ProductFeelings
        fields = ["feeling"]


class ProductSkintypeSerializer(serializers.ModelSerializer):
    skin_type = serializers.CharField(source='name')

    class Meta:
        model  = ProductSkintype
        fields = ['skin_type']


class ProductIngredientSerializer(serializers.ModelSerializer):
    ingredient = serializers.CharField(source='name')

    class Meta:
        model  = ProductIngredient
        fields = ['ingredient']


class ProductSerializer(serializers.ModelSerializer):
    category   = serializers.CharField(source='category.category_name')
    feelings   = ProductFeelingsSerializer(read_only=True, many=True)
    skin_types = ProductSkintypeSerializer(read_only=True, many=True)
    ingredient = ProductIngredientSerializer(read_only=True, many=True)

    class Meta:
        model  = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model  = Category
        fields = '__all__'