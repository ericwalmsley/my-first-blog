from django.urls import path #django's path fx
from . import views #importing all views from the blog app

urlpatterns = [
    path('', views.post_list, name='post_list'), #assings a view called post_list to the root URL
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new , name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]