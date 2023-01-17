from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from ..models import Question, Answer, Comment
from ..forms import CommentForm

from django.contrib.auth.decorators import login_required





@login_required(login_url='login')
def comment_question_create(request, question_id):
    """
    CommentForm, get, post
    """
    question = get_object_or_404(Question, id=question_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            cmt = form.save(commit=False)
            cmt.author = request.user
            cmt.question = question
            cmt.save()
            return redirect("{}#comment_{}".format(resolve_url("detail", question_id=question_id), cmt.id))

    else:
        form = CommentForm()

    return render(request, "boardapp/comment_form.html", {"form":form})

@login_required(login_url='login')
def comment_question_modified(request, comment_id):
    """
    댓글 내용 수정 - CommentForm, get, post, 성공 시 detail
    """
    cmt = get_object_or_404(Comment, id=comment_id)
    if request.method=="POST":
        form = CommentForm(request.POST, instance=cmt)
        if form.is_valid():
            form.save()
            return redirect("{}#comment_{}".format(resolve_url("detail", question_id=form.question_id), form.id))
    else:
        form = CommentForm(instance=cmt)
    return render(request, "boardapp/comment_form.html", {"form":form})

@login_required(login_url='login')
def comment_question_delete(request, comment_id):
    """
    댓글 내용 삭제 - CommentForm, get, 성공 시 detail
    """
    cmt = get_object_or_404(Comment, id=comment_id)
    cmt.delete()

    return redirect("detail", question_id=cmt.question.id)

@login_required(login_url='login')
def comment_answer_create(request, answer_id):
    """
    CommentForm, get, post
    """
    answer = get_object_or_404(Answer, id=answer_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            cmt = form.save(commit=False)
            cmt.author = request.user
            cmt.answer = answer
            cmt.save()
            return redirect("{}#comment_{}".format(resolve_url("detail", question_id=cmt.answer.question.id), cmt.id))

    else:
        form = CommentForm()

    return render(request, "boardapp/comment_form.html", {"form":form})

@login_required(login_url='login')
def comment_answer_modified(request, comment_id):
    """
    댓글 내용 수정 - CommentForm, get, post, 성공 시 detail
    """
    cmt = get_object_or_404(Comment, id=comment_id)
    if request.method=="POST":
        form = CommentForm(request.POST, instance=cmt)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect("{}#comment_{}".format(resolve_url("detail", question_id=comment.answer.question.id), comment.id))
    else:
        form = CommentForm(instance=cmt)
    return render(request, "boardapp/comment_form.html", {"form":form})

@login_required(login_url='login')
def comment_answer_delete(request, comment_id):
    """
    댓글 내용 삭제 - CommentForm, get, 성공 시 detail
    """
    cmt = get_object_or_404(Comment, id=comment_id)
    cmt.delete()

    return redirect("detail", question_id=cmt.answer.question.id)

