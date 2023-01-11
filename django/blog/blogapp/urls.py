"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # http://127.0.0.1:8000/blogs/write/
    path('write/', views.post_write, name='post_write'),
    # http://127.0.0.1:8000/blogs/4/
    path('<int:pk>/', views.post_detail, name='post_detail'),
    # http://127.0.0.1:8000/blogs/comment_create/
    path('comment_create/', views.comment_create, name='comment_create'),
    # http://127.0.0.1:8000/blogs/post/like/
    path('post/like', views.post_like, name='post_like'),
]
