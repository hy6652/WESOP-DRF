from rest_framework.views       import APIView
from rest_framework.response    import Response
from rest_framework.permissions import IsAuthenticated

from carts.serializers import CartSerializer

from carts.models import Cart


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