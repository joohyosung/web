from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def register(request):
    """
    회원가입
    get - 비어있는 form
    post - 바인딩 form
    """
    if request.method =="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserForm()
    return render(request, "userapp/register.html", {"form":form})