from app.models import Task 

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from app.serializers import TaskSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser 



class TaskList(APIView):
    permission_classes = (IsAuthenticated,)
    """
    List all Task with current Group in User.
    """
    def get(self, request, format=None):
        task_dataset = Task.objects.filter(created_by__in=User.objects.values_list('id').filter( \
            groups__in=Group.objects.values_list('id').filter(user=request.user)))
        serializer = TaskSerializers(task_dataset, many=True)
        return Response(serializer.data)
