from django import forms
from .models import Profile
from django.contrib.auth.models import User

class ProfilesForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'content']