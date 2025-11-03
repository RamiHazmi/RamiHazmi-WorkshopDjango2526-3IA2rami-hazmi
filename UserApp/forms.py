from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):
    class meta:
        model=User
        fields= ['first_name','last_name','affiliation','nationality','email','password1','password2' ]
        widgets ={
            'email' : forms.EmailInput(
                {
                    'placeholder': "Email universitaire"
                }
            ),
            'password1' : forms.PasswordInput(),
            'password2' : forms.PasswordInput(),

                
        }