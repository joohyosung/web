from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('custom_form/', views.custom_form, name='custom_form'),
    path('django_form/', views.django_form, name='django_form'),

    # 함수형 뷰
    path('musician_function_create/', views.musician_create, name='musician_function_create'),
    path('musician_function_list/', views.musician_list, name='musician_function_list'),

    # https://127.0.0.1:8000/exam/musician_function_detail/<int:pk>/
    path('musician_function_detail/<int:pk>/', views.musician_detail, name='musician_function_detail'),
    path('musician_function_edit/<int:pk>/', views.musician_edit, name='musician_function_edit'),
    path('musician_function_remove/<int:pk>/', views.musician_remove, name='musician_function_remove'),
    # 클래스 뷰
]