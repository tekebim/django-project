from django.urls import path
from todo import views

app_name = 'todo'

urlpatterns = [
    # ex: /todo/
    path('', views.index, name='index'),
    # ex: /todo/edit
    path('edit/<int:task_id>', views.edit, name='edit'),
]
