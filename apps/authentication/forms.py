from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.password_validation import (
    MinimumLengthValidator,NumericPasswordValidator,CommonPasswordValidator,UserAttributeSimilarityValidator)
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):

    email= forms.EmailField(validators=[EmailValidator('email is invalid')],required=True)
    first_name = forms.CharField(max_length=100,required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model =User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
            self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
            self.fields['username'].widget.attrs.update({'class': 'form-control'})
            self.fields['password1'].widget.attrs.update({'class': 'form-control'})
            self.fields['password2'].widget.attrs.update({'class': 'form-control'})
            self.fields['email'].widget.attrs.update({'class': 'form-control'})

            # for fieldname in ['username','email','password1','password2']:
            #     self.fields[fieldname].help_text=None

class LoginForm(AuthenticationForm):
      
    class Meta:
        model = User 
        fields= ['username','password']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['username'].widget.attrs.update({'class': 'form-control'})
            self.fields['password'].widget.attrs.update({'class': 'form-control'})