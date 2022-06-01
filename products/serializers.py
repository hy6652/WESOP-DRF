from rest_framework import serializers

from products.models import Feeling, Product, ProductFeelings, ProductSkintype

class ProductFeelingsSerializer(serializers.ModelSerializer):
    feeling = serializers.CharField(source='name')

    class Meta:
        model = ProductFeelings
        fields = ["feeling"]


class ProductSkintypeSerializer(serializers.ModelSerializer):
    skin_type = serializers.CharField(source='name')

    class Meta:
        model = ProductSkintype
        fields = ['skin_type']


class ProductSerializer(serializers.ModelSerializer):
    category   = serializers.CharField(source='category.category_name')
    feelings   = ProductFeelingsSerializer(read_only=True, many=True)
    skin_types = ProductSkintypeSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'