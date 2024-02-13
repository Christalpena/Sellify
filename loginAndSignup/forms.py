from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']


        def clean_email(self):
            email = self.cleaned_data.get(self.fields['email'])
            if CustomUser.objects.filter(email = email).exists():
                raise forms.ValidationError(u'This email is already in use.')
            return email

class CompleteProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name','profile_photo')


class LoginCustomUserForm(AuthenticationForm):
    fields = ['email','password']

