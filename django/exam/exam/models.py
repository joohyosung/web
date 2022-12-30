from django.db import models

# Create your models here.
# 필드 기본 옵션
# null, blank => False
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'person'
    # __str__함수는 makemigration 대상이 아님
    def __str__(self) -> str:
        return self.first_name + ', ' + self.last_name

# Musician 테이블
# first_name    단문
# last_name     단문
# instrument    단문
class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)   
    instrument = models.CharField(max_length=100)

    class Meta :
        db_table = 'musician'
    def __str__(self) -> str:
        return self.first_name + ', ' + self.instrument

# Album 테이블
# artist        외래키(FK)
# name          단문
# release_date  날짜
# num_stars     숫자

class Album(models.Model):
    # 외래키 : 테이블 join 시 필요한 컬럼(부모 자식관계로 정의됨) / on_delete=models.CASCADE : 부모 삭제 시 자식도 삭제
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self) -> str:
        return self.name

# primary key : 테이블 생성 시 하나만 지정 가능
#               unique, not null
# 기본키 필드를 지정하지 않는다면 장고가 기본으로 무조건 생성함
class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self) -> str:
        return self.name    

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='질문')
    pub_date = models.DateTimeField(verbose_name='작성날짜')

    def __str__(self) -> str:
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='연결된 질문')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0, verbose_name='투표')

    def __str__(self) -> str:
        return self.choice_text