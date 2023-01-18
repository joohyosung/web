from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = "home.html"

    def dispatch(self, request, *args, **kwargs):
        """
        요청이 들어올 때 로그인 정보가 있다면 contents로 이동 없다면 home
        """
        if not request.user.is_anonymous:
            return redirect("contents")
            
        return super().dispatch(request, *args, **kwargs)
    

class ContentsView(TemplateView):
    template_name = "contents/main.html"