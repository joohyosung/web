from django.db import models

# Create your models here.

class Book(models.Model):
    code = models.CharField(max_length=4,primary_key=True,verbose_name='도서코드')
    title = models.CharField(max_length=100,verbose_name='도서명')
    author = models.CharField(max_length=50,verbose_name='저자')
    price = models.IntegerField(verbose_name='도서정가')
    register_dttm = models.DateTimeField(verbose_name='등록날짜', auto_now_add=True)

    class Meta:
        db_table = 'booktbl'