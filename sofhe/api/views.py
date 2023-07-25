from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import action

from django.contrib.auth.models import User

from .models import Event
from .serializers import EventSerializer


class EventTask(ModelViewSet):

    serializer_class = EventSerializer
    queryset = Event.objects.none()

    @action(detail=True, methods=['post'])
    def addUserTask(self, request, pk=None):
        current_user = User.objects.filter(pk=pk).last()
        data = request.data
        if current_user:
            Event.objects.create(
                user=current_user, title=data['title'], description=data['description'], credit=data['credit'], task_datetime=data['task_datetime'], status=int(data['status']))
            return Response({'message': 'Event Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'User not recognized'}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        current_user = User.objects.filter(pk=pk).last()
        data_query = current_user.event_set.all().order_by('-pk')
        serializer = EventSerializer(data_query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        pass

    def partial_update(self, request, taskId, pk=None):
        current_user = User.objects.filter(pk=pk).last()
        try:
            getevent = Event.objects.get(pk=taskId, user=current_user)
            data = request.data
            if getevent:
                getevent.title = data['title']
                getevent.description = data['description']
                getevent.credit = data['credit']
                getevent.task_datetime = data['task_datetime']
                getevent.status = int(data['status'])
                getevent.save()
                return Response({'message': 'Event Edited'}, status=status.HTTP_202_ACCEPTED)
        except:
            return Response({'message': 'Something went wrong'}, status=status.HTTP_404_NOT_FOUND)


    def destroy(self, request, taskId, pk=None):
        current_user = User.objects.filter(pk=pk).last()
        try:
            getevent = Event.objects.get(pk=taskId, user=current_user)
            getevent.delete()
            return Response({'message': 'Event deleted'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Something went wrong'}, status=status.HTTP_404_NOT_FOUND)



