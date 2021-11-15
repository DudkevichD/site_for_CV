from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import FeedbackModels


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль')


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModels
        fields = ('title', 'content', 'file', 'contacts')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'contacts': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            }
