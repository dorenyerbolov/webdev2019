from django.urls import path
from api import views

# urlpatterns = [
#     path('task_lists/', views.task_list),
#     path('task_lists/<int:pk>/', views.task_list_details),
#     path('task_lists/<int:pk>/tasks/', views.task_list_tasks)
# ]


urlpatterns = [
    path('task_lists/', views.TaskList.as_view()),
    path('task_lists/<int:pk>/', views.TaskListDetails.as_view()),
    path('task_lists/<int:pk>/tasks/', views.TaskListTasks.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
]
