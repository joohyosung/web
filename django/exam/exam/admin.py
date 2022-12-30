from django.contrib import admin
from .models import *
# Register your models here.
# 어드민 사이트에서 모델 사용하려면 등록 필수
admin.site.register(Question)
admin.site.register(Choice)