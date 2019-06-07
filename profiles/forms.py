from django import forms
from .models import Profile
from django.contrib.auth.models import User

class ProfilesForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'content']

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control profileInput',
                    'placeholder': 'ex) zamanchu@sookmyung.ac.kr',
                    'type': 'email',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control profileInput2',
                    'placeholder': 'ex) 안녕하세요!',
                    'type': 'TextArea',
                }
            ),
        }