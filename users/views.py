from rest_framework.decorators import api_view, APIView
from rest_framework.response   import Response

from users.serializers import RegistrationSerailzer


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = RegistrationSerailzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        

# @api_view(['POST', ])
# def registration_view(request):
#     if request.method == 'POST':
#         serializer = RegistrationSerailzer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)