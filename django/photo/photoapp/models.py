from django.db import models

# Create your models here.
# model 생성 : class로 작성
# 사용할 필드에 적절한 타입을 부여
# CharField() : max_length 값 무조건 필요
# TextField() : 긴 문자열
class Photo(models.Model):
    title = models.CharField(max_length=50)
    auther = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()