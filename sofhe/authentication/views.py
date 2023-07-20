from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from .serializers import Login
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


@api_view(['POST'])
def login_post(request):
    return 1


@api_view(['GET'])
def total_user(request):
    user_query = User.objects.all()
    serializer = Login(user_query, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def logout_user(request):
    data = request.data
    try:
        token = RefreshToken(data['token'])
        token.blacklist() 
        return Response({'message': 'Logged out'}, status=status.HTTP_200_OK)
    except TokenError:
        return Response({'message': 'Bad Token'}, status=status.HTTP_400_BAD_REQUEST)
