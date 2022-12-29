
from django.urls import path, include
from .views import *
urlpatterns = [
    path("", todo_list, name="todo_list"),
    path("<int:pk>/", todo_detail, name="todo_detail"),
    path("new/", todo_register, name="todo_register"),
    path("<int:pk>/edit/", todo_edit, name="todo_edit"),
    path("<int:pk>/done/", todo_done, name="todo_done"),
    path("done/", done_list, name="done_list"),
]
