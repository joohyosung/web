from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from ..models import Question, Answer
from ..forms import AnswerForm

from django.contrib.auth.decorators import login_required




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
            return redirect("{}#answer_{}".format(resolve_url("detail", question_id=question_id), answer.id))

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

            return redirect("{}#answer_{}".format(resolve_url("detail", question_id=answer.question_id), answer.id))

    else:
        form = AnswerForm(instance=answer)

    return render(request, "boardapp/answer_form.html", {"form":form})

@login_required(login_url='login')
def answer_delete(request, answer_id):
    """
    답변삭제 - 삭제 성공 시 detail로 이동
    """
    answer = get_object_or_404(Answer, id=answer_id)        

    if request.user != answer.author:
        return redirect('detail', question_id=answer.question_id)

    answer.delete()
    return redirect('detail', question_id=answer.question_id)