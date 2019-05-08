from django_filters import rest_framework as filters
from api.models import Task


class TaskFilter(filters.FilterSet):
    class Meta:
        model = Task
        fields = ('name', )
