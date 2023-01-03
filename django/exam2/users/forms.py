# 장고 User 객체
# 속성 - username, password, email, first_name, last_name

# 사용자 생성
# from django.contrib.auth.models import User
# user = User.objects.create_user('john', 'john@google.com', 'johnpassword')
# user.save()

# # 비밀번호 변경
# u = User.objects.get(username='john')
# u.set_password('newjohnpassword')
# u.save()

# 권한 확인
# user.is_authenticated

# 사용자 인증(사용자가 아이디랑 비밀번호를 입력 => 승인)
# select count(*) from user where username 'john' and password = 'johnpassword'
# count가 1이라면 상속
# from django.contrib.auth import authenticate, login
# user = authenticate(request, username=username, password=password)   # select count(*) from user where username 'john' and password = 'johnpassword'

# login(request,user)

# 일반 form 상속, 모델 form 상속

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):

    # email = forms.EmailField(label='이메일', black = True) 부모가 정의한 상태

    # 상속 시 email은 필수요소가 아니기 때문에 재정의를 통해 필수요소로 변경
    email = forms.EmailField(label='이메일')

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username','email']