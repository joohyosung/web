
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 회원가입
    path("register/", views.register, name="register"),
    # 로그인, 로그아웃 : 직접구현 or 쟝고 view 이용
    path("login/", auth_views.LoginView.as_view(template_name="userapp/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
