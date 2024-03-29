from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # fields = '__all__'
        # exclude = ('slug')


# class SignInForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']