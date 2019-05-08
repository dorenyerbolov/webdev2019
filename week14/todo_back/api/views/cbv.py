from api.serializers import TaskSerializer, TaskListSerializer, UserSerializer
from api.models import TaskList as TaskListModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.http import Http404


class TaskList(APIView):
    def get(self, request):
        task_lists = TaskListModel.objects.all()
        serializer = TaskListSerializer(task_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskListDetails(APIView):
    def get_object(self, pk):
        try:
            return TaskListModel.objects.get(id=pk)
        except TaskListModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task_list = self.get_object(pk)
        serializer = TaskListSerializer(task_list)
        return Response(serializer.data)

    def put(self, request, pk):
        task_list = self.get_object(pk)
        serializer = TaskListSerializer(instance=task_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        task_list = self.get_object(pk)
        task_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskListTasks(APIView):
    def get_object(self, pk):
        try:
            return TaskListModel.objects.get(id=pk)
        except TaskListModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        task_list = self.get_object(pk)
        tasks = task_list.task_set.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        task_list = self.get_object(pk)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(task_list=task_list)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

