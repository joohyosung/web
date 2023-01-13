"""
config URL Configuration

Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from . import views
from django.urls import path

urlpatterns = [
    # http://127.0.0.1:8000/photo/ => views.py에 home 함수가 응답
    path("", views.home, name='home'),
    # http://127.0.0.1:8000/photo/new/ + get, post
    path("new/", views.post, name='post'),
    # http://127.0.0.1:8000/photo/2
    # path("<int:pk>/", views.detail, name="detail"),
    path("serialize_detail/<int:pk>/", views.serialize_detail, name="detail"),

    # http://127.0.0.1:8000/photo/remove
    path("serialize_detail/<int:pk>/remove/", views.remove, name="remove"),
    # http://127.0.0.1:8000/photo/edit
    path("serialize_detail/<int:pk>/edit/", views.edit, name="edit")
]
