from django import forms
import json
from .models import Build


class BuildForm(forms.ModelForm):
    class Meta:
        model = Build
        fields = [
            'title',
            'author',
            'guide',
            'characters'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-build', 'id': 'form-title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Anonymous', 'class': 'form-build', 'id': 'form-author'}),
            'guide': forms.Textarea(attrs={'class': 'form-build', 'id': 'form-guide'}),
            'characters': forms.HiddenInput(attrs={'class': 'form-build', 'id': 'form-characters'})
        }
