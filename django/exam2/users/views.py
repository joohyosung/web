from django.shortcuts import render, redirect
from .forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

# Create your views here.
def signup(request):
    """
    회원가입
    """
    if request.method == "POST":
        # post로 넘어오는 모든 입력값을 form과 연결(바인딩)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
        
        
    return render(request, "users/register.html", {"form":form})  

def isLogin(request):
    if request.method == "POST":
        # username, password 가져오기
        username = request.POST['username']
        password = request.POST['password']
        # db 확인(사용자의 입력값과 데이터베이스 내용 확인)
        user = authenticate(request, username=username,password=password)
        # 세션에 정보 저장
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, "users/login.html")

def common_logout(request):
    # 세션해제
    logout(request)
    return redirect('index')

class CustomPasswordChangeView(PasswordChangeView):
    """
    PasswordChangeView 안에

    바뀐 비밀번호로 세션을 동기화 -> 사용자가 바뀐 비밀번호로 로그인을 하지 않아도 된다.
    update_session_auth_hash(self.request, form.user) :
    """
    success_url = reverse_lazy("users:login")
    template_name = "users/password_change.html"

