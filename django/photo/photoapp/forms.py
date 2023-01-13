from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    # Meta 내부 클래스로 반드시 필요함
    class Meta:
        model = Photo
        # 모델에서 사용할 필드들을 나영(튜플, 리스트)
        fields = "__all__"