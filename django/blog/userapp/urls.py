from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("signup/", views.sign_up, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="userapp/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="userapp/logout.html"), name="logout"),
]
