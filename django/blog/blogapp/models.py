from django.db import models
from userapp.models import User
from taggit.managers import TaggableManager
# Create your models here.

# 글 등록, 수정, 삭제, 조회
# 글 번호(자동생성), 작성자, 제목, 내용, 작성날짜, 수정날짜

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    title = models.CharField(verbose_name='제목', max_length=255, blank=False)
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(blank=True, null=True, verbose_name='이미지')      # pillow 라이브러리 필요
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='작성날짜') # auto_now_add=True 글이 처음 등록될 대 자동으로 입력
    modified_at = models.DateTimeField(auto_now=True, verbose_name='수정날짜')   # auto_now=True 글을 수정할 때마다 자동으로 입력
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    tags = TaggableManager()

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    post = models.ForeignKey(Post,  verbose_name="원본글", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    create_at = models.DateTimeField(
        auto_now_add=True, verbose_name="작성날짜"
    )  # auto_now_add = True 글이 처음 등록될 때 자동으로 입력
    modified_at = models.DateTimeField(
        auto_now=True, verbose_name="수정날짜"
    )  # auto_now = True 글을 수정할 때마다 자동으로 입력

    def __str__(self) -> str:
        return "%s-%s" % (self.id, self.user)