
from django.urls import path
from . import views
urlpatterns = [
    path("", views.list, name='list'),
    path("<int:pk>/", views.detail, name='detail'),
    path("<int:pk>/edit/", views.update, name='update'),
    path("<int:pk>/remove/", views.remove, name='remove'),
    path("create/", views.create, name='create'),
]
