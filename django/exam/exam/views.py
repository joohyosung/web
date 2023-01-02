from django.shortcuts import render, redirect, get_object_or_404
from .forms import NameForm, MusicianForm
from .models import Musician
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 

# Create your views here.
def index(request):
    return render(request, 'exam/index.html')

def custom_form(request):
    # get / post

    errors =[]

    if request.method == 'POST':
        # name 가져오기
        name = request.POST['name'] # request.POST.get('name')
        # 유효성 검증 - 이름이 홍길동이어야 한다.
        if name != '홍길동':
            # 에러 메시지 전송 - 원래 페이지로 돌려보내기
            errors.append('이름을 확인해주세요.')
        else:
            return redirect('index')


    return render(request, 'exam/custom_form.html',{'errors':errors})

def django_form(request):
    
    # get / post - Form 클래스 사용

    if request.method == 'POST':
        # 사용자의 입력값을 form 데이터로 수신
        form = NameForm(request.POST)
        if form.is_valid(): # 바인딩 여부 검증, max_length < 20, required 검증
            return redirect('index')
    else:
        form = NameForm()

    return render(request, 'exam/django_form.html',{'form':form})

# musician 추가
def musician_create(request):
    """
    get : 비어있는 form 보여주기
    post : 넘어오는 데이터 form에 바인딩하기
    """
    if request.method == "POST":
        form = MusicianForm(request.POST)
        if form.is_valid(): # bound 여부 ,max_length, black,null -> False
            form.save()
            return redirect('index')
    else:
        form = MusicianForm()

    return render(request, "exam/create.html", {"form":form})

# musician 삭제
def musician_remove(request, pk):
    """
    pk에 해당하는 musician 삭제
    """
    # pk musician 찾기
    musician = get_object_or_404(Musician, pk=pk)
    # 삭제 -delete()
    musician.delete()
    # 리스트 이동
    return redirect('musician_function_list')
# musician 수정
def musician_edit(request, pk):
    """
    get : pk에 해당하는 musician form에 담아 전송
    post : 입력한 데이터 form에 담아 수정
    """
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == "POST":
        # 수정을 위해 입력한 데이터 form에 담기
        form = MusicianForm(request.POST, instance=musician)
        # 유효성 검사
        if form.is_valid():
            musician = form.save()
            return redirect("musician_function_detail", pk=musician.pk)
        
    else:
        form = MusicianForm(instance=musician)
    return render(request, "exam/edit.html", {"form":form})

# musician 전체조회
def musician_list(request):
    """
    전체 musician 추출 후 전송
    """
    # all
    list = Musician.objects.all()

    # render
    return render(request, 'exam/list.html', {'list':list})

# musician 한명조회
def musician_detail(request, pk):
    """
    pk에 해당하는 musician 조회 후 전송
    1. 조회, 전송 -> 템플릿 파일을 처음부터 디자인
    2. 조회, form 담기, 전송 -> 템플릿 파일에서 form.as_p or for문 돌려서 만들기
    """
    musician = get_object_or_404(Musician, pk=pk)
    form = MusicianForm(instance = musician)
    return render(request, 'exam/detail.html', {"form":form}) 

# 클래스 뷰
# TemplateView == render
# RedirectView == redirect
# ListView - 모델 설정

class SampleView(TemplateView):
    template_name = 'exam/sample.html'

class MusicianListView(ListView):
    model = Musician
    template_name = 'exam/list.html'# exam/musician_list.html
    context_object_name = 'list'    # 생략 가능(단, 모델소문자_list : context_object_name = 'list' 기본값)

class MusicianDetailView(DetailView):
    model = Musician
    template_name = 'exam/musician_detail.html'
    
class MusicianCreateView(CreateView):
    template_name = 'exam/create.html'
    form_class = MusicianForm
    success_url = reverse_lazy('musician_class_list')

class MusicianUpdateView(UpdateView):
    template_name = 'exam/edit.html'
    model = Musician
    fields = '__all__'
    context_object_name = 'form'
    # 성공 시 pk를 가지고 detail로 이동
    # 부모의 get_success_url 재정의
    def get_success_url(self) -> str:
        return reverse_lazy('musician_class_detail', args=[self.object.pk])

class MusicianDeleteView(DeleteView):
    model = Musician
    success_url = reverse_lazy('musician_class_list')

    # get 오버라이딩
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)