from django import forms
from .models import Message

# 모델폼
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '쪽지 내용을 입력하세요.',
                }
            ),
        }

class AddMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']

        widgets = {
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control message_content',
                    'placeholder': '쪽지 내용을 입력하세요.',
                    'rows': 'none',
                }
            )
        }
        labels = {
            'content': ''
        }