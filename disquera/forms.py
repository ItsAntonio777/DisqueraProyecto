from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Comment, Order


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Order

        fields = [
            'full_name',
            'address',
            'city',
            'postal_code'
        ]

        widgets = {

            'full_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Tu nombre completo'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Tu dirección',
                'rows': 4
            }),

            'city': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Tu ciudad'
            }),

            'postal_code': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Código postal'
            }),
        }