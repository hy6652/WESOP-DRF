from rest_framework import serializers

from carts.models import Cart


class CartSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    def create(self, validated_data):
        user     = validated_data.get('user')
        quantity = validated_data.get('quantity')
        product  = validated_data.get('product')

        if not quantity:
            raise serializers.ValidationError({'you need more than 1 product'})

        cart, is_created = Cart.objects.get_or_create(
                                user     = user,
                                product  = product,
                                defaults = {'quantity':quantity}
                            )
        
        if not is_created:
            cart.quantity += quantity
            cart.save()

        return cart

    class Meta:
        model = Cart
        fields = '__all__'