
from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/board/ : 전체 게시물
    path('', views.board_list, name='board_list'),
    # http://127.0.0.1:8000/board/create/ : 게시물 작성
    path('create/', views.board_write, name='board_write'),
    # http://127.0.0.1:8000/board/1/ : 게시물 상세보기
    path('<int:pk>/', views.board_detail, name='board_detail'),
    
]