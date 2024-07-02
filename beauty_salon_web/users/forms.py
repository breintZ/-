from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Введите имя пользователя',
            'class': 'form-input'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Введите пароль',
            'class': 'form-input'
        }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Введите имя',
            'class': 'form-input'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Введите фамилию',
            'class': 'form-input'
        }
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Введите имя пользователя',
            'class': 'form-input'
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Введите адрес эл. почты',
            'class': 'form-input'
        }
    ))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-input',
            'placeholder': 'Введите номер телефона'
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Введите пароль',
            'class': 'form-input'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Подтвердите пароль',
            'class': 'form-input'
        }
    ))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-input'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-input'
        }
    ))
    image = forms.ImageField(widget=forms.FileInput(
        attrs={
            'class': 'custom-file-input',
        }
    ), required=False)
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-input',
            'readonly': True
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-input',
        }
    ))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-input',
        }
    ))


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email', 'phone')