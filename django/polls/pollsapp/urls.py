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
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'pollsapp'

urlpatterns = [
    # path('', TemplateView.as_view(template_name = 'polls/index.html'), name = 'index'),
    # 함수형 뷰
    # path('',views.Index, name = 'index'),
    # path('<int:pk>/',views.Detail, name = 'detail'),
    # path('<int:pk>/vote/',views.Vote, name = 'vote'),
    # path('<int:pk>/results/',views.Results, name = 'results'),

    # 클래스 뷰
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.PollDetailView.as_view(), name='details'),
    path('<int:pk>/results/', views.PollResultView.as_view(), name='results'),

    path('<int:pk>/vote/',views.Vote, name = 'vote'),
    
]
