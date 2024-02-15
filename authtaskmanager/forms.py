from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class CustomUserCreationForm(UserCreationForm):
    is_admin = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('is_admin',)
