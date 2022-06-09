from rest_framework.decorators       import APIView
from rest_framework.response         import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import RegistrationSerailzer


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = RegistrationSerailzer(data=request.data)

        if serializer.is_valid():
            user    = serializer.save()
            refresh = RefreshToken.for_user(user)

            data = {}

            data['username'] = user.username
            data['email']    = user.email
            data['token']    = {
                                    'refresh': str(refresh),
                                    'access' : str(refresh.access_token)
                                }
            return Response(data, status=201)
        return Response(serializer.errors, status=400)