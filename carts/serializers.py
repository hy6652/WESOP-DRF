from rest_framework import serializers

from carts.models import Cart

class CartSerializer(serializers.ModelSerializer):
    user    = serializers.StringRelatedField(read_only=True)
    product = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Cart
        fields = '__all__'