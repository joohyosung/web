from django.shortcuts import render,redirect, get_object_or_404

from .models import Board
from .forms import BoardForm

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

# Create your views here.
def board_list(request):
    """
    Board 목록 전체 추출
    """
    # 전체 게시물 추출
    all_boards = Board.objects.order_by('-register_dttm')

    # 사용자가 요청한 페이지 번호
    page = request.GET.get('page', 1)

    # Paginator 객체를 이용한 보여줄 페이지 결정
    paginator = Paginator(all_boards, 10)

    boards = paginator.get_page(page)

    return render(request, "boardapp/board_list.html", {"boards":boards})

@login_required(login_url='login')
def board_write(request):
    """
    Board 새 글 작성
    get
    """
    if request.method =="POST":
        form = BoardForm(request.POST)

        print("##############",request.POST['tags'])
        if form.is_valid():
            board = form.save(commit=False) # 유저 정보가 없기 때문에 commit=False
            board.writer = request.user
            board.save()

            # 태그 저장
            form.save_m2m()

            return redirect("board_list")
    else:
        form = BoardForm()
    return render(request, "boardapp/board_create.html",{"form":form})

def board_detail(request, pk):
    """
    상세보기
    """
    board = get_object_or_404(Board, pk=pk)

    return render(request, "boardapp/board_detail.html",{'board':board})