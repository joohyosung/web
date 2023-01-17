from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    # http://127.0.0.1:8000/user/login/
    path('login/', auth_views.LoginView.as_view(template_name='userapp/login.html'), name='login'),
    # http://127.0.0.1:8000/user/logout/
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    # PasswordChangeView : 비밀번호 변경, 바뀐 비밀번호로 업데이트하고, 세션도 계속 유지
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name="userapp/password_change.html", success_url=reverse_lazy("index")), name="password_change"),
    
    path('password_reset/', views.UserPasswordResetView.as_view(), name="password_reset" ),
    path('password_reset/done/', views.UserPasswordResetDoneView.as_view(), name="password_reset_done" ),
    path('reset/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name="password_reset_confirm" ),
    path('reset/done/', views.UserPasswordResetCompleteView.as_view(), name="password_reset_complete" ),
    

    # django 자체 view는 비밀번호 리셋 시에는 이메일로 링크 전송하고 그 링크를 통해 비밀번호를 재지정하도록 되어 있음

]
