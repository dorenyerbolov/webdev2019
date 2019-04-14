from django.shortcuts import render
from api.models import TaskList, Task
from django.http import JsonResponse


# Create your views here.


def task_list(request):
    task_list = [t.to_json() for t in TaskList.objects.all()]
    return JsonResponse(task_list, safe=False)


def task_list_details(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(task_list.to_json())


def task_list_tasks(requies, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    tasks = task_list.task_set.all()
    json_tasks = [t.to_json() for t in tasks]

    return JsonResponse(json_tasks, safe=False)
