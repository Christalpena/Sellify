from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from userAccount.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

class CompleteProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name','profile_photo')


class LoginCustomUserForm(AuthenticationForm):
    fields = ['email','password']

