from django import forms
from .models import Meeting

# 모델폼
class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['category', 'title', 'body', 'date', 'start_time', 'end_time']
        # fields = ['title']
        # fields = '__all__'
        
        widgets = {
            'category': forms.Select(
                attrs={
                    'class': 'form-control form-control-lg',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'ex) 같이 보드게임해요',
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': '내용을 입력하세요.',
                    'rows': '5',
                }
            ),
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control form-control-lg',
                },
            ),
            'start_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control form-control-lg',
                }
            ),
            'end_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control form-control-lg',
                }
            )
        }

        # widgets = {
        #     'category': forms.Select(
        #         attrs={
        #             'class': 'form-control',
        #         }
        #     ),
        #     'title': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': 'ex) 같이 보드게임해요',
        #         }
        #     ),
        #     'body': forms.Textarea(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': '내용을 입력하세요.',
        #             'rows': '5',
        #         }
        #     ),
        #     'date': forms.DateInput(
        #         attrs={
        #             'type': 'date',
        #             'class': 'form-control',
        #         },
        #     ),
        #     'start_time': forms.TimeInput(
        #         attrs={
        #             'type': 'time',
        #             'class': 'form-control',
        #         }
        #     ),
        #     'end_time': forms.TimeInput(
        #         attrs={
        #             'type': 'time',
        #             'class': 'form-control',
        #         }
        #     )
        # }