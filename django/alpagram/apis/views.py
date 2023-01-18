from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from users.forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class BaseView(View):
    """
    클라이언트로부터 요청을 받아 JsonResponse로 응답하는 뷰
    """
    @staticmethod
    def response(result={}, status=200):
        return JsonResponse(result, status=status)

class UserCreateView(BaseView):

    # get / post 방식 판별
    @csrf_exempt # cseftoken 검증하지 말 것    
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # 비밀번호 암호화
            user.set_password(form.cleaned_data['password'])
            user.save()
            return self.response({"error":False, "message":"Successfully"}, status=200)
        else:
            return self.response({"error":True, "message":form.errors}, status=400)