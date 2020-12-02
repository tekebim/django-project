from django.urls import path

from . import views

urlpatterns = [
    # ex: /todo/
    path('', views.index, name='index'),
    # ex: /todo/edit
    path('edit/<int:task_id>', views.edit, name='edit')
]
