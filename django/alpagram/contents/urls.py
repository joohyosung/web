from django.urls import path
from . import views

from django.urls import reverse_lazy


urlpatterns = [
    # contents 홈
    # contents/ name='contents'
    path('', views.ContentsView.as_view(), name="contents"),
    
]