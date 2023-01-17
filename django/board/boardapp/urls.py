from django.urls import path
from .views import base_views, question_views, answer_views, comment_views, vote_views

urlpatterns = [
    path('', base_views.index, name='index'),
    ### questions
    # http://127.0.0.1:8000/board/question/detail/
    path('<int:question_id>/', base_views.detail, name='detail'),
    # http://127.0.0.1:8000/board/question/create/
    path('question/create/', question_views.question_create, name='question_create'),
    # http://127.0.0.1:8000/board/question/modified/1/
    path('question/modified/<int:pk>/', question_views.question_modified, name='question_modified'),
    # http://127.0.0.1:8000/board/question/delete/1/
    path('question/delete/<int:pk>/', question_views.question_delete, name='question_delete'),

    ### answers
    # http://127.0.0.1:8000/board/answer/create/1/
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    # http://127.0.0.1:8000/board/answer/modified/1/
    path('answer/modified/<int:answer_id>/', answer_views.answer_modified, name='answer_modified'),
    # http://127.0.0.1:8000/board/answer/delete/1/
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    ### comment
    # http://127.0.0.1:8000/board/comment/create/question/question_id/
    path('comment/create/question/<int:question_id>/', comment_views.comment_question_create, name='comment_question_create'),
    # http://127.0.0.1:8000/board/comment/modified/question/comment_id/
    path('comment/modified/question/<int:comment_id>/', comment_views.comment_question_modified, name='comment_question_modified'),
    # http://127.0.0.1:8000/board/comment/delete/question/comment_id/
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_question_delete, name='comment_question_delete'),

    # http://127.0.0.1:8000/board/comment/create/answer/answer_id/
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_answer_create, name='comment_answer_create'),
    # http://127.0.0.1:8000/board/comment/modified/answer/comment_id/
    path('comment/modified/answer/<int:comment_id>/', comment_views.comment_answer_modified, name='comment_answer_modified'),
    # http://127.0.0.1:8000/board/comment/delete/answer/comment_id/
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_answer_delete, name='comment_answer_delete'),

    ### vote
    # http://127.0.0.1:8000/board/question/vote/question_id/
    path('question/vote/<int:question_id>/', vote_views.vote_question, name='vote_question'),
    # http://127.0.0.1:8000/board/answer/vote/answer_id/
    path('answer/vote/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),
]
