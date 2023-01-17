from django.shortcuts import render, get_object_or_404
from ..models import Question, QuestionCount
from django.core.paginator import Paginator
from django.db.models import Q, Count
from tools.utils import get_client_ip


# Create your views here.
def index(request):
    """
    Question 전체 추출(작성날짜 최신순)
    """ 

    # 사용자가 요청한 페이지 번호
    page = request.GET.get('page',1)

    # 검색어 받기
    keyword = request.GET.get('keyword','')

    # 정렬 기준 받기
    so = request.GET.get('so','recent') # sort 기준 : recent(기본), recommend, popular

    # 전체 게시물 추출
    if so == "recommend":
        all_questions = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter','-created_dttm')
    elif so == "popular":
        all_questions = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer','-created_dttm')
    else:
        all_questions = Question.objects.order_by('-created_dttm')

    # 전체 리스트에서 검색어가 들어간 리스트만 추출(질문 제목, 질문 내용, 질문 작성자, 답변 작성자)
    # Q : OR 조건으로 데이터 조회, distinct() : 중복 제거
    if keyword:
        all_questions = all_questions.filter(Q(title__icontains=keyword)|Q(content__icontains=keyword)).distinct()
            
    # Paginator 객체를 이용한 보여줄 페이지 결정
    paginator = Paginator(all_questions, 10)

    questions = paginator.get_page(page)

    return render(request, 'boardapp/question_list.html', {"questions":questions, "page":page, "keyword":keyword, "so":so})

def detail(request, question_id):
    """
    question_id에 맞는 질문 상세 추출
    조회수 증가 : ip 얻어내기
    """
    # 사용자가 요청한 페이지 번호
    page = request.GET.get('page',1)

    # 검색어 받기
    keyword = request.GET.get('keyword','')

    # 정렬 기준 받기
    so = request.GET.get('so','recent') # sort 기준 : recent(기본), recommend, popular

    questions = get_object_or_404(Question, pk=question_id)

    # ip 받아오기
    ip = get_client_ip(request)
    # 현재 질문에 대한 조회수 찾기
    cnt = QuestionCount.objects.filter(ip=ip, question=questions).count()

    if cnt == 0:
        qc = QuestionCount(ip=ip, question=questions)
        qc.save()

        if questions.view_cnt:
            questions.view_cnt += 1
        else:
            questions.view_cnt = 1
        questions.save()

    return render(request, 'boardapp/question_detail.html', {"question":questions, "page":page, "keyword":keyword, "so":so})