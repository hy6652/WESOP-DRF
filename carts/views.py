from rest_framework             import generics
from rest_framework.views       import APIView
from rest_framework.response    import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions  import ValidationError

from carts.serializers import CartSerializer

from carts.models    import Cart
from products.models import Product


class CartListGV(generics.ListAPIView):
    queryset         = Cart.objects.all()
    serializer_class = CartSerializer


# class CartCreateView(generics.ListCreateAPIView):
#     queryset           = Cart.objects.all()
#     serializer_class   = CartSerializer
#     permission_classes = [IsAuthenticated]


class CartListView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request):
        carts      = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)


class CartDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return Response({'your cart info does not exist'}, status=400)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        cart = Cart.objects.get(pk=pk)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
    
    def delete(self, request, pk):
        cart = Cart.objects.get(pk=pk)
        cart.delete()
        return Response(status=204)


# class CartView(View):
#     @author
#     def post(self, request):
#         try:
#             data = json.loads(request.body)

#             cart, created  = Cart.objects.get_or_create(
#                 user       = request.user,
#                 product_id = data['product_id']
#             )
#             if not created and cart.quantity < 20:
#                 cart.quantity += 1
#                 cart.save()
#                 return JsonResponse({'message': 'SUCCESS'}, status=200)
#             elif not created and cart.quantity > 19:
#                 return JsonResponse({'message': 'INVALID_QUANTITY'}, status=200)
#             else:
#                 return JsonResponse({'message': 'SUCCESS'}, status=201)

#         except Cart.DoesNotExist:
#             return JsonResponse({'message': 'CART_DOES_NOT_EXIT'}, status=400)
#         except KeyError:
#             return JsonResponse({'message': 'KEY_ERROR'}, status=400)

#     @author
#     def get(self, request):
#         user  = request.user
#         carts = Cart.objects.filter(user=user)

#         if not carts.exists():
#             return JsonResponse({'message': 'INVALID_USER'}, status=400)

#         result = [{
#             'userId'      : user.id,
#             'cartId'      : cart.id,
#             'quantity'    : cart.quantity,
#             'productId'   : cart.product.id,
#             'productName' : cart.product.name,
#             'productSize' : cart.product.size,
#             'totalPrice'  : int(cart.quantity * cart.product.price)
#         } for cart in carts]
#         return JsonResponse({'message': result}, status=200)

#     @author
#     def patch(self, request, cart_id):
#         try:
#             data = json.loads(request.body)
#             user = request.user
#             quantity = data['quantity']

#             if quantity <= 0 or quantity >= 21:
#                 return JsonResponse({'message': 'INVALID_QUANTITY'}, status=400)

#             if Cart.objects.filter(id=cart_id).exists():
#                 cart          = Cart.objects.get(id=cart_id, user=user)
#                 cart.quantity = data['quantity']
#                 cart.save()
#                 return JsonResponse({'message': 'QUANTITY_CHANGED'}, status=201)

#             return JsonResponse({'message': 'CART_DOES_NOT_EXIT'}, status=404)

#         except KeyError:
#             return JsonResponse({'message': 'KEY_ERROR'}, status=400)

#     @author
#     def delete(self, request):
#         try:
#             cart_ids = request.GET.getlist('cart_ids')
#             user     = request.user

#             if not cart_ids:
#                 return JsonResponse({'message': 'LIST_EMPTY'}, status=400)

#             Cart.objects.filter(id__in=cart_ids, user_id=user).delete()
#             return JsonResponse({'message': 'CART_DELETED'}, status=200)

#         except ValueError:
#             return JsonResponse({'message': 'VALUE_ERROR'}, status=400)
