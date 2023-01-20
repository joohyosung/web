from django.urls import path
from . import views

urlpatterns = [
    # 회원가입
    # users/create/ name='user_create'
    path('users/create/', views.UserCreateView.as_view(), name="user_create"),
    path('users/profile/delete', views.UserProfileImageDelete.as_view(), name="user_profile_delete"),
    path('users/profile/update', views.UserProfileImageUpdate.as_view(), name="user_profile_update"),

    # 새글 등록
    path('contents/new/', views.ContentCreateView.as_view(), name="contents_new"),
]