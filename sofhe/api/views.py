from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


@permission_classes([IsAuthenticated])
class TaskView(APIView):
    def post(self, request, format=None):
        data = request.data
        print(data)
        return Response({'data': 1}, status=status.HTTP_201_CREATED)
