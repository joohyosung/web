# 바인딩 Form - 데이터랑 form이랑 연결된 상태
# form = NameForm(request.POST)

from django import forms
from .models import Musician

class NameForm(forms.Form):
    # 일반 form

    # input type='text' 생성
    name = forms.CharField(max_length=20, label='Your Name')

    # 추가 검증 시 메소드의 이름은 clean이 들어가도록 해야 함
    # clean_요소명(필드명) : name 필드에 대해 유효성 검사
    def clean_name(self):
        cleaned_data =  super().clean()
        name = cleaned_data['name']

        if name != '홍길동':
            raise forms.ValidationError('이름을 확인해주세요.')

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__' # fields = [필요한 필드] or (필요한 필드)
        # exclude =['제외할 필드']