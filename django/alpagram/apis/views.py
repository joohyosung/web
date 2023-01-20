from django.shortcuts import render, get_object_or_404
from django.views import View
from users.models import Profile

from django.http import JsonResponse
from users.forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate, login

from contents.models import Content, Image
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class BaseView(View):
    """
    클라이언트로부터 요청을 받아 JsonResponse로 응답하는 뷰
    """
    @staticmethod
    def response(result={}, status=200):
        return JsonResponse(result, status=status)

@method_decorator(login_required,name="dispatch")
class ContentCreateView(BaseView):
    """
    이미지의 텍스트 가져온 후 입력
    """
    def post(self, request):
        text = request.POST.get('text').strip()
        content = Content.objects.create(user=request.user, text=text)
        
        for idx, file in enumerate(request.FILES.values()):
            Image.objects.create(content=content, img=file, order=idx)

        return self.response({"error":False, "message":"Successfully"},status=200)

@method_decorator(login_required,name="dispatch")
class UserProfileImageUpdate(BaseView):
    """
    사용자 프로필 사진을 사용자가 선택한 이미지로 변경
    """
    def post(self, request):
        
        # 사용자가 보낸 이미지 가져오기
        image = request.FILES['file']

        profile = get_object_or_404(Profile, user=request.user)
        profile.img = image
        profile.save()

        return self.response({"error":False, "messange":"Successfully"}, status=200)

class UserProfileImageDelete(BaseView):
    """
    사용자 프로필 사진을 default.png로 변경
    """
    def get(self, request):
        """
        현재 로그인 사용자의 이미지 profile/default.png로 변경
        """
        profile = get_object_or_404(Profile, user=request.user)
        profile.img = 'profile/default.png'
        profile.save()

        return self.response({"error":False, "messange":"Successfully"}, status=200)

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
            # 로그인 처리 : authenticate(), login()
            new_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if new_user is not None:
                login(request, new_user)
                

            return self.response({"error":False, "message":"Successfully"}, status=200)
        else:
            return self.response({"error":True, "message":form.errors}, status=400)