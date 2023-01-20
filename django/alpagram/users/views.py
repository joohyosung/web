from django.shortcuts import render
from django.views.generic.base import TemplateView

from contents.models import Content
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required,name='dispatch')
class ProfileEdit(TemplateView):
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 로그인 사용자의 게시물 개수
        context['contents'] = Content.objects.filter(user=self.request.user)
        return context