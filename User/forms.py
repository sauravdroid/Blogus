from django.contrib.auth.models import User
from django import forms


class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields =['username','first_name','last_name','password','email']
