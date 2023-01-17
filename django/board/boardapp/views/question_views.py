from django.shortcuts import render, redirect, get_object_or_404
from ..models import Question
from ..forms import QuestionForm

from django.contrib.auth.decorators import login_required



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

@login_required(login_url='login')
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