from django.urls import path

from . import views

urlpatterns = [
    # ex: /todo/
    path('', views.index, name='index')
]
