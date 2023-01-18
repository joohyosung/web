from django.urls import path
from . import views

from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 로그인 / 로그아웃
    # login/ name='login'
    path('login/', auth_views.LoginView.as_view(template_name="home.html", success_url=reverse_lazy('contents')), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]