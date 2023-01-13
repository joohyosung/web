from django.db import models
from django.contrib.auth.models import User

# 질문 모델
# 제목(Char-200), 내용(Text), 작성날짜(datetime), 수정날짜(datetime)
class Question(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    author = models.ForeignKey(User, verbose_name="글쓴이", on_delete=models.CASCADE)
    created_dttm = models.DateTimeField(auto_now_add=True, verbose_name='작성날짜')
    modified_dttm = models.DateTimeField(auto_now=True, verbose_name='수정날짜')

# 답변 모델
# 질문(어떤 질문에 대한 답변인지 파악), 답변 내용, 작성날짜, 수정날짜
class Answer(models.Model):
    question = models.ForeignKey(Question, verbose_name="질문", on_delete=models.CASCADE)
    content = models.TextField(verbose_name='내용')
    author = models.ForeignKey(User, verbose_name="글쓴이", on_delete=models.CASCADE)
    created_dttm = models.DateTimeField(auto_now_add=True, verbose_name='작성날짜')
    modified_dttm = models.DateTimeField(auto_now=True, verbose_name='수정날짜')
