from django.shortcuts import render, redirect, get_object_or_404
from ..models import Question, Answer
from ..forms import QuestionForm

from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def vote_question(request, question_id):
    """
    질문 추천 등록 / 성공 시 detail
    질문 찾은 후 question.voter.add(로그인 사용자)
    """
    question = get_object_or_404(Question, id=question_id)

    if request.user != question.author:
        question.voter.add(request.user)
    else:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.") 

    return redirect('detail', question_id=question_id)

def vote_answer(request, answer_id):
    """
    답변 추천 등록 / 성공 시 detail
    답변 찾은 후 answer.voter.add(로그인 사용자)
    """
    answer = get_object_or_404(Answer, id=answer_id)

    if request.user != answer.author:
        answer.voter.add(request.user)
    else:
        messages.error(request, "본인이 작성한 글은 추천할 수 없습니다.") 

    return redirect('detail', question_id=answer.question.id)