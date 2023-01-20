from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Content

class HomeView(TemplateView):
    template_name = "home.html"

    def dispatch(self, request, *args, **kwargs):
        """
        요청이 들어올 때 로그인 정보가 있다면 contents로 이동 없다면 home
        """
        if not request.user.is_anonymous:
            return redirect("contents")
            
        return super().dispatch(request, *args, **kwargs)
    
# 이렇게 작성해야 하는 부분을 아래처럼 간단하게 처리 가능
# @method_decorator(login_required,name="dispatch")
# class ContentsView(TemplateView):
#     template_name = "contents/main.html"

#     @login_required
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

@method_decorator(login_required,name="dispatch")
class ContentsView(TemplateView):
    template_name = "contents/main.html"

    def get_context_data(self, **kwargs):
        """
        로그인 사용자의 작성글 전체 가져오기
        """
        context = super().get_context_data(**kwargs)
        context['contents'] = Content.objects.filter(user=self.request.user)
        return context