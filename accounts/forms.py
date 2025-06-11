from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re


# User signup form including email validation for common domains
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # Allow only specific domain endings
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r".+@.+\.(com|net|org|io|co\.uk|gov|edu)$",
                        email.lower()):
            raise ValidationError(
                "Please enter a valid email domain (e.g. .com, .org).")
        return email
