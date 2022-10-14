from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from .models import Schedule


class ScheduleUpdateForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ('first_name', 'last_name', 'subject', 'link', 'link2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                                                            'placeholder': 'Логін'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                                             'type': 'password',
                                                             'placeholder': 'Пароль'}))


