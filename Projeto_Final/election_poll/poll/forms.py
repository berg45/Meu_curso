from django import forms
from .models import Poll, Option

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a pergunta da enquete'})
        }

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['option_text']
        widgets = {
            'option_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a opção'})
        }
