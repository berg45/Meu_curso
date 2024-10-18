# autentication/forms.py

from django import forms
from django.contrib.auth.models import User

class RegistroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.set_password(self.cleaned_data['senha'])
        if commit:
            user.save()
        return user
