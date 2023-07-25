from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RefreshSerializer
# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class AuthenticationUser(APIView):

    serializer_class = RefreshSerializer
    
    def post(self, request, format=None, *args, **kwargs):
        refreshtoken = RefreshSerializer(self.request.data['token'], many=False)
        try:
            token = RefreshToken(refreshtoken.data['refreshtoken'])
            token.blacklist() 
            return Response({'message': 'Logged out'}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({'message': 'Bad Token'}, status=status.HTTP_400_BAD_REQUEST)

