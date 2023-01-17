"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from boardapp.views import base_views

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('boardapp.urls')),
    path('user/', include('userapp.urls')),
    path('', base_views.index),
    
    # django-allauth에서 제공하는 urls 가져오기
    path('accounts/', include('allauth.urls')),

    # path('', include("django.contrib.auth.urls")),
    # path('password_reset/', auth_views.PasswordChangeView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    
]
