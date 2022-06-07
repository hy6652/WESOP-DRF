from rest_framework import serializers

from carts.models import Cart
from products.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    user       = serializers.StringRelatedField(read_only=True)
    # product_id = serializers.ReadOnlyField(source='product.id')
    # product = serializers.StringRelatedField(read_only=True)
    
    # def create(self, validated_data):
        
        # quantity = validated_data.get('quantity')
        # product = validated_data.get('product')

        # cart, is_created = Cart.objects.get_or_create(
        #                         quantity=quantity,
        #                         product=product
        #                     )

        # if not quantity:
        #     raise serializers.ValidationError({'you need more than 1 product'})
        # # if not product:
        # #     raise serializers.ValidationError({'you must select a product'})
        
        # cart, create = Cart.objects.get_or_create(
        #     **validated_data
        # )
        # cart.quantity += quantity
        # cart.save()

        # return Cart.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.quantity = validated_data.get('quantity', instance.quantity)
    #     instance.save()
    #     return instance

    class Meta:
        model = Cart
        fields = '__all__'