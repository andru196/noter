from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Note


class LogForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        help_texts = {
        'username': ""
    }

class SaveForm(ModelForm):
    class Meta:
        model = Note
        fields = ("id", 'text', 'color', 'locked', 'protected')
        widgets = {
            'color': forms.TextInput(attrs={'type': "color"}),
        }


class IDForm(forms.Form):
    id = forms.CharField(max_length=10, required=True)


class RegForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_ver = forms.CharField(widget=forms.PasswordInput())