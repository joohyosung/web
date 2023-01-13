from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """
    Question 전체 추출(작성날짜 최신순)
    """ 
    # 전체 게시물 추출
    all_questions = Question.objects.order_by('-created_dttm')
    # 사용자가 요청한 페이지 번호
    page = request.GET.get('page',1)
    # Paginator 객체를 이용한 보여줄 페이지 결정
    paginator = Paginator(all_questions, 10)

    questions = paginator.get_page(page)

    return render(request, 'boardapp/question_list.html', {"questions":questions})

def detail(request, question_id):
    """
    question_id에 맞는 질문 상세 추출
    """
    questions = get_object_or_404(Question, pk=question_id)
    all_answers = questions.answer_set.all().order_by('-created_dttm')
    page = request.GET.get('page',1)
    paginator = Paginator(all_answers, 5)
    answers = paginator.get_page(page)
    print(all_answers)

    return render(request, 'boardapp/question_detail.html', {"question":questions, "answers":answers})

@login_required(login_url='login')
def question_create(request):
    """
    get - 비어있는 form
    post - 바인딩된 form
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            questions = form.save(commit=False)
            questions.author = request.user
            questions.save()
            return redirect('index')
    else:
        form = QuestionForm()
    return render(request, 'boardapp/question_form.html', {'form':form})

def question_modified(request, pk):
    """
    질문 수정 - form 사용
    수정 완료 후 detail로 이동
    """
    # 수정 질문 찾기
    question = get_object_or_404(Question, id=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('detail', question_id=pk)
    else:
        form = QuestionForm(instance=question)
        return render(request, 'boardapp/question_modified.html', {'form':form})

@login_required(login_url='login')
def question_delete(request, pk):
    """
    pk값과 일치한 질문 삭제 후 전체 리스트
    """
    question = get_object_or_404(Question, id=pk)
    if request.user != question.author:
        return redirect('detail', question_id=pk)

    question.delete()
    return redirect('index')


@login_required(login_url='login')
def answer_create(request, question_id):
    """
    답변등록
    get - 비어있는 form
    post - 바인딩된 form
    """
    questions = get_object_or_404(Question, pk=question_id)
    # answer = Answer(question=questions, content=request.POST['content'])
    # answer.save()
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = questions
            answer.author = request.user
            answer.save()
            return redirect('detail', question_id=question_id)

    else:
        form = AnswerForm()
    return render(request, 'boardapp/question_detail.html', {'form':form, "question":questions})

@login_required(login_url='login')
def answer_modified(request, answer_id):
    """
    답변수정 - AnswerForm 사용(answer_form.html), 수정 성공 시 detail로 이동
    """
    answer = get_object_or_404(Answer, id=answer_id)        

    if request.user != answer.author:
        return redirect('detail', question_id=answer.question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.save()

            return redirect('detail', question_id=answer.question_id)
    else:
        form = AnswerForm(instance=answer)

    return render(request, "boardapp/answer_form.html", {"form":form})

def answer_delete(request, answer_id):
    """
    답변삭제 - 삭제 성공 시 detail로 이동
    """
    answer = get_object_or_404(Answer, id=answer_id)        

    if request.user != answer.author:
        return redirect('detail', question_id=answer.question_id)

    answer.delete()
    return redirect('detail', question_id=answer.question_id)






