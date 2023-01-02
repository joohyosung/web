from django.contrib import admin
from .models import *
# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # 관리자 페이지에서 필드의 순서, 사용할 필드
    # fields = ['pub_date', 'question_text']
     fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Date Information", {"fields":['pub_date']})
     ]
     inlines = [ChoiceInline]
     list_display = ['question_text', 'pub_date']

admin.site.register(Question, QuestionAdmin)