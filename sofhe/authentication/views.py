from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
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


class AuthenticationUser(GenericAPIView):

    serializer_class = None

    def post(self, request, *args, **kwargs):
        data = self.request.data
        try:
            token = RefreshToken(data['token'])
            token.blacklist() 
            return Response({'message': 'Logged out'}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({'message': 'Bad Token'}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def logout_user(request):
#     data = request.data
#     try:
#         token = RefreshToken(data['token'])
#         token.blacklist() 
#         return Response({'message': 'Logged out'}, status=status.HTTP_200_OK)
#     except TokenError:
#         return Response({'message': 'Bad Token'}, status=status.HTTP_400_BAD_REQUEST)
