from django import forms
from .models import Question, Answer

# QuestionForm 작성 - title, content
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields =['title','content']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields =['content']