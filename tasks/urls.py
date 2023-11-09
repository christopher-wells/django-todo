from django.urls import path

from . import views

app_name = "tasks"

urlpatterns = [
    path('', views.TaskListView.as_view(), name='index'),
    path('add_task/', views.CreateTaskView.as_view(), name='add_task'),
    path('<int:pk>/update/', views.UpdateTaskView.as_view(), name='update_task'),
    path('<int:pk>/delete/', views.DeleteTaskView.as_view(), name='delete_task'),
]
