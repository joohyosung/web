from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from django.contrib.auth import authenticate, login

# Create your views here.
def register(request):
    """
    회원가입
    get - 비어있는 form / post - 바인딩 form
    """
    if request.method == "POST":
        users = UserForm(request.POST)
        if users.is_valid():
            users.save()

            # 회원가입 완료 후 로그인 처리도 해주고 싶다면?
            username = users.cleaned_data.get('username')
            password = users.cleaned_data.get('password1')

            # db 확인(사용자의 입력값과 데이터베이스 내용과 확인)
            user = authenticate(request, username=username, password=password)

            # 세션에 정보 저장
            if user is not None:
                login(request, user)
                return redirect('index')
            
    else:
        users = UserForm()
    return render(request, "userapp/register.html", {'form':users})