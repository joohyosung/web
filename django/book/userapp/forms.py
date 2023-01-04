# form 생성
# 일반 form, 모델 form 상속
# UserForm 생성 == User 모델 (django.contrib.auth.models)
# UserCreationForm : User 모델 + Form 기능
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]  # password는 필수로 추가됨 

