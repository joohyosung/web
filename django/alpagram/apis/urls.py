from django.urls import path
from . import views

urlpatterns = [
    # 회원가입
    # users/create/ name='user_create'
    path('users/create/', views.UserCreateView.as_view(), name="user_create")
]