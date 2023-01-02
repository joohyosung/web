from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def Index(request):
    """
    질문 전체 보기 구현
    """
    # 질문 전체 리스트 : 가장 최신 순으로
    question_list = Question.objects.order_by('-pub_date')
    return render(request, "polls/index.html", {"question_list":question_list})

def Detail(request, pk):
    """
    pk에 해당하는 choice, question 필요함
    question = get_object_or_404(Question, pk=pk)
    choice = Choice.objects.filter(question_id = pk)
    """
    question = get_object_or_404(Question, pk=pk)
    return render(request, "polls/detail.html", {"question":question})

def Vote(request, pk):
    """
    pk에 해당하는 질문 가져오기 / 사용자의 선택된 choice 가져오기
    질문을 통해 choice에 접근한 후 투표 수 증가
    """
    question = get_object_or_404(Question, pk=pk)

    if request.method == "POST":
        
        try: 
            selected_choice = question.choice_set.get(pk=request.POST['choice'])

        except KeyError as e:
            return render(request, "polls/detail.html",{"question":question, "error_message":"선택하지 않았습니다."})

        else:
            selected_choice.votes += 1
            selected_choice.save()
            return redirect("pollsapp:results",pk=pk)
    return redirect('index')

def Results(request, pk):
    """
    pk에 해당하는 질문 가져오기
    """
    question = get_object_or_404(Question,pk=pk)
    return render(request, 'polls/result.html', {"question":question})

#######################################################################################
# 제네릭 뷰                                                                            
# template_name : 사용할 html 파일 지정                                                 
# context_object_name : 모델 소문자(DetailView), 모델 소문자_list(ListView) ==> 기본값   
#                       기본값 사용하지 않을 거라면 추가 지정                            
#######################################################################################

class IndexView(ListView):
    # model = Question  == Question.objects.all()
    template_name = 'polls/index.html'

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")

    context_object_name = 'question_list'

class PollDetailView(DetailView):
    template_name = 'polls/detail.html'
    model = Question
    
    

class PollResultView(DetailView):
    template_name = 'polls/result.html'
    model = Question
    