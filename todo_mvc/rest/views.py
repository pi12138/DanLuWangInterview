from rest_framework import viewsets
from rest_framework.response import Response

from todo_mvc.models import Task

from todo_mvc.rest.serializers import TaskSerializer

import datetime


class TaskViewSet(viewsets.ViewSet):
    """
    任务视图集
    """
    def list(self, requets):
        query_set = Task.objects.all()
        ser = TaskSerializer(instance=query_set, many=True)
        return Response(ser.data)

    def create(self, request):
        data = request.data
        data['create_time'] = datetime.datetime.now()

        ser = TaskSerializer(data=data)
        if not ser.is_valid():
            return Response({'error': ser.errors, 'msg': '数据不合法'}, status=400)

        ser.save()
        return Response(ser.data)
