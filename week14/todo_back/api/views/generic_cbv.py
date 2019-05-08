from api.serializers import TaskSerializer, TaskListSerializer
from api.models import TaskList as TaskListModel, Task as TaskModel
from api.filters import TaskFilter

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from django.http import Http404


class TaskList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskListModel.objects.filter(created_by=self.request.user)

    def get_serializer_class(self):
        return TaskListSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskListDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskListModel.objects.filter(created_by=self.request.user)

    def get_serializer_class(self):
        return TaskListSerializer


class TaskListTasks(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    # TODO DjangoFilterBackend
    filter_class = TaskFilter

    # TODO SearchFilter
    search_fields = ('name', 'id')

    # TODO OrderingFilter
    ordering_fields = ('name', 'id')
    # ordering = ('id')

    def get_queryset(self):
        try:
            task_list = TaskListModel.objects.filter(created_by=self.request.user).get(
                id=self.kwargs[self.lookup_field])
        except TaskListModel.DoesNotExist:
            raise Http404

        return TaskModel.objects.filter(task_list=task_list)

    def perform_create(self, serializer):
        try:
            task_list = TaskListModel.objects.filter(created_by=self.request.user).get(
                id=self.kwargs[self.lookup_field])
        except TaskListModel.DoesNotExist:
            raise Http404

        serializer.save(task_list=task_list)
