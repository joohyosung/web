from django.db import models
from usersapp.models import User
from taggit.managers import TaggableManager
# title, contents, writer(User), register_dttm
class Board(models.Model):
    title = models.CharField(verbose_name="제목", max_length=128)
    contents = models.TextField(verbose_name="내용")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    register_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    
    tags = TaggableManager()
