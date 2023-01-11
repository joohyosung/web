from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(request):
    """
    get - 비어있는 form
    post - 바인딩 form
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegisterForm()
    return render(request, 'usersapp/register.html', {"form":form})
    