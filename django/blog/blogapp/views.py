from django.shortcuts import render,redirect,get_object_or_404
from .forms import PostForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# 비동기식 처리에 대한 응답
from django.http import JsonResponse

# Create your views here.
def post_list(request):
    """
    전체 글 목록 추출
    """
    # order_by : 작성날짜 최신순
    posts = Post.objects.order_by('-create_at')
    return render(request, "blogapp/post_list.html",{'posts':posts}) 

@login_required(login_url="login")
def post_write(request):
    """
    글 작성 : 로그인 필수
    get - 비어있는 form, post - 바인딩 form
    """
    if request.method == "POST":
        # request.POST : text 가져옴, request.FILES : file 가져옴
        form =PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # commit : 최종반영, rollback : 취소
            # 글쓴이 추가 <== 로그인 사용자
            post.user = request.user
            post.save()
            # 태그 저장(manytomany 필드 저장)
            form.save_m2m()
            
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "blogapp/post_write.html", {'form':form})

def post_detail(request, pk):
    """
    pk에 해당하는 글 조회
    """
    post = get_object_or_404(Post, pk=pk)

    # 좋아요
    is_liked = False

    # 조회한 post에 로그인 유저가 좋아요를 눌렀는지 여부
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    return render(request, "blogapp/post_detail.html", {"post":post, "is_liked":is_liked})

@login_required(login_url="login")
def comment_create(request):
    """
    댓글등록 : get 요청은 없음, post 요청만 처리
    """
    if request.method == "POST":
        # content, post_id(원본글번호) 가져오기
        content = request.POST['content']
        post_id = request.POST.get('post_id','').strip()

        if content and post_id:
            # 삽입(user : 로그인 사용자, post : 원본글번호, content : 댓글내용)
            comment = Comment.objects.create(user=request.user, post_id=post_id, content=content)
            # post_detail 돌아가기
            return redirect('post_detail', pk=comment.post.id)
    
    messages.error(request, '댓글을 입력해주세요.')
    return redirect("post_detail", pk=post_id)

def post_like(request):
    """
    비동기식 유형 : 좋아요 클릭
    """
    # 글번호 가져오기
    post_id = request.POST['id']

    # 글번호에 해당하는 게시물 찾기
    post = get_object_or_404(Post, id=post_id)

    # 로그인 사용자가 현재 게시물에 좋아요 누른 정보가 있는지 확인
    is_liked = post.likes.filter(id=request.user.id).exists()

    if is_liked:
        post.likes.remove(request.user)
        is_liked =False
    else:
        post.likes.add(request.user)
        is_liked = True

    return JsonResponse({"likes":post.likes.count(), "is_liked":is_liked})
