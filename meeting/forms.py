from django import forms
from .models import Meeting

# 일반폼
# class MeetingPost(forms.Form):
#     category = forms.ChoiceField(
#         label='카테고리',
#         choices=[('식사', '식사'), ('문화', '문화'), ('스포츠', '스포츠/레저'), ('취미', '취미/힐링'), ('스터디', '스터디'), ('기타', '기타')],
#         )
#     title = forms.CharField(
#         label='제목',
#         help_text='만남 제목을 입력하세요',
#         )
#     body = forms.CharField(
#         label='만남 소개글',
#         help_text='만남 소개글을 입력하세요',
#         )
#     date = forms.DateField(
#         label='날짜',
#         widget=forms.widgets.DateInput(attrs={'type': 'date'}),
#         )
#     start_time = forms.TimeField(
#         label='시작 시각',
#         widget=forms.widgets.TimeInput(attrs={'type': 'time'}),
#     )
#     end_time = forms.TimeField(
#         label='종료 시각',
#         widget=forms.widgets.TimeInput(attrs={'type': 'time'}),
#     )


# 모델폼
class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        # fields = ['title', 'body', 'date', 'start_time', 'end_time']
        # fields = ['title']
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '제목을 입력하세요.',
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '내용을 입력하세요.',
                }
            )
            # 'end_time': DateTimeWidget(),
        }