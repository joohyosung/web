from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # http://127.0.0.1:8000/user/login/
    path('login/', auth_views.LoginView.as_view(template_name='userapp/login.html'), name='login'),
    # http://127.0.0.1:8000/user/logout/
    path('', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

]
