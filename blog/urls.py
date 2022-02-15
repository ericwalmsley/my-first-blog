from django.urls import path #django's path fx
from . import views #importing all views from the blog app

urlpatterns = [
    path('', views.post_list, name='post_list'), #assings a view called post_list to the root URL
]

