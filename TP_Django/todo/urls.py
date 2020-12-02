from django.urls import path
from todo import views

app_name = 'todo'

urlpatterns = [
    # ex: /todo/
    path('', views.index, name='index'),
    # ex: /todo/edit
    path('edit/<int:task_id>', views.edit, name='edit'),
    # ex: /todo/delete
    path('delete/<int:task_id>', views.delete, name='delete'),
    # ex: /todo/finish
    path('finish/<int:task_id>', views.finish, name='finish'),
    # ex: /todo/delete/all
    path('delete/all', views.deleteAll, name='deleteAll'),
    # ex: /todo/delete/done
    path('delete/done', views.deleteDone, name='deleteDone'),
]
