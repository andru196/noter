from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Note


class LogForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class SaveForm(ModelForm):
    class Meta:
        model = Note
        fields = ("id", 'text', 'color', 'locked', 'protected')


class IDForm(forms.Form):
    id = forms.CharField(max_length=10)


class RegForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_ver = forms.CharField(widget=forms.PasswordInput())