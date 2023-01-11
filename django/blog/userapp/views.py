from django.shortcuts import render, redirect
from .forms import UserForm
# Create your views here.
def sign_up(request):
    """
    회원가입
    get - 비어있는 form
    post - 바인딩된 userform
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserForm()
    return render(request, "userapp/signup.html",{"form":form})