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
            'character_1'
        ]
    title = forms.CharField(label='Title', max_length=120)  
    author = forms.CharField(label='Author', max_length=50)
    guide = forms.CharField(label='Guide', widget=forms.Textarea)
    character_1 = forms.CharField(widget=forms.HiddenInput())

    def clean_character_1(self, *args, **kwargs):
        jdata = self.cleaned_data['character_1']
        try:
            json_data = json.loads(jdata)
        except:
            raise forms.ValidationError()
        return jdata