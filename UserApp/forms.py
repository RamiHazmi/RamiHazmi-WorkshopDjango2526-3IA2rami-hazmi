from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model= User
        fields =['username','first_name','last_name',
                 'email','affiliation','nationality',
                 'password1','password2']
        widgets ={
            'email' : forms.EmailInput(attrs={
                'placeholder': "Email universitaire"
            }),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
    """def save(self, commit = True):
        user= super().save(commit=False)
        user.role="participant"
        if commit:
            user.save()
        return user"""