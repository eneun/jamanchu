from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django import forms
from .models import Meeting

# 모델폼
class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        # fields = ['title', 'body', 'date', 'start_time', 'end_time']
        # fields = ['title']
        fields = '__all__'
        
        widgets = {
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
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
            ),
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                },
            ),
            'start_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control',
                }
            ),
            'end_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control',
                }
            )
        }