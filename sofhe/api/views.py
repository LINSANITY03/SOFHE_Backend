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
def addUserTask(request, pk):
    current_user = User.objects.filter(id=pk).last()
    data = request.data
    if current_user:
        Event.objects.create(
            user=current_user, title=data['_title'], description=data['_description'], credit=data['_income'], task_datetime=data['_datetime'], status=int(data['_status']))
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


@api_view(['POST'])
def editUserTask(request, taskId, pk):

    current_user = User.objects.filter(id=pk).last()
    getevent = Event.objects.get(id=taskId, user=current_user)
    data = request.data
    if getevent:
        getevent.title = data['_title']
        getevent.description = data['_description']
        getevent.credit = data['_income']
        getevent.task_datetime = data['_datetime']
        getevent.status = int(data['_status'])
        getevent.save()
        return Response({'data': 1}, status=status.HTTP_202_ACCEPTED)
    else:
        return Response({'data': 0}, status=status.HTTP_404_NOT_FOUND)
