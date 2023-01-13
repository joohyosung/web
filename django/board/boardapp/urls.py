from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    ### questions
    # http://127.0.0.1:8000/board/question/detail/
    path('<int:question_id>/', views.detail, name='detail'),
    # http://127.0.0.1:8000/board/question/create/
    path('question/create/', views.question_create, name='question_create'),
    # http://127.0.0.1:8000/board/question/modified/1/
    path('question/modified/<int:pk>/', views.question_modified, name='question_modified'),
    # http://127.0.0.1:8000/board/question/delete/1/
    path('question/delete/<int:pk>/', views.question_delete, name='question_delete'),

    ### answers
    # http://127.0.0.1:8000/board/answer/create/1/
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    # http://127.0.0.1:8000/board/answer/modified/1/
    path('answer/modified/<int:answer_id>/', views.answer_modified, name='answer_modified'),
    # http://127.0.0.1:8000/board/answer/delete/1/
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]
