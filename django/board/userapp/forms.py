from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


# Userform 생성
class UserForm(UserCreationForm):

    # email 필수 필드로 정의
    email = forms.EmailField(label='이메일')
    class Meta:
        model = User
        fields =['username','email']