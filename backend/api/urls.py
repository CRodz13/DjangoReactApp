from django.urls import path
from .views import TaskList, TaskDetail


urlpatterns = [
    path('', TaskList.as_view(), name="api-overview"),
    path('task-list/', TaskList.as_view(), name="task-list"),
    path('task-detail/<str:pk>/', TaskDetail.as_view(), name="task-detail"),
    path('task-create/', TaskList.as_view(), name="task-create"),
    path('task-update/<str:pk>/', TaskDetail.as_view(), name="task-update"),
    path('task-delete/<str:pk>/', TaskDetail.as_view(), name="task-delete"),
]
