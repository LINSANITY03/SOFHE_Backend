from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.contrib.auth.models import User

from .models import Event
from .serializers import EventSerializer


# @permission_classes([IsAuthenticated])
class TaskView(APIView):
    def post(self, request, format=None):
        data = request.data
        user_data = User.objects.filter(id=data['_user']).last()
        if user_data:
            print(data)
            print(data['_datetime'])
            Event.objects.create(
                user=user_data, title=data['_title'], description=data['_description'], credit=data['_income'], task_datetime=data['_datetime'], status=data['_status'])
            return Response({'data': 1}, status=status.HTTP_201_CREATED)
        else:
            return Response({'data': 0}, status=status.HTTP_404_NOT_FOUND)


# @permission_classes([IsAuthenticated])
@api_view(['GET'])
def userTask(request, pk):
    current_user = User.objects.filter(id=pk).last()
    data_query = current_user.event_set.all().order_by('-id')
    serializer = EventSerializer(data_query, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
    # return Response({"message": "Hello, world!"})
