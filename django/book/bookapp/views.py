from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# Create your views here.
def list(request):
    """
    전체 도서 목록 추출
    """
    book_list = Book.objects.all()
    return render(request, "bookapp/book_list.html",{'book_list':book_list})

def detail(request, pk):
    """
    pk에 해당하는 상세 정보 추출
    """
    book = get_object_or_404(Book, pk=pk)

    return render(request, "bookapp/book_detail.html",{"book":book})

def update(request, pk):
    """
    get   :  pk에 해당하는 상세 정보 추출
    post  :  정보 수정
    """
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("detail", pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, "bookapp/book_update.html",{"form":form})

def remove(request, pk):
    """
    pk에 해당하는 book 삭제 후 리스트로 이동
    """
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('list')

def create(request):
    """
    get : BookForm 비어 있는 상태로
    post : BookForm에 입력값 바인딩 후 저장 -> 리스트로 이동
    """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form = BookForm()
    return render(request, "bookapp/book_create.html", {"form":form})

