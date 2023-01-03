from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),

    # custom login / logout
    # path('login/', views.isLogin, name='login'),
    # path('logout/', views.common_logout, name='logout'),

    # djago.contrib.auth.urls 이용
    # path('accounts/', include("django.contrib.auth.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', views.CustomPasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
]
