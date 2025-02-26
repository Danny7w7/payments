from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from app.models import *

class UserForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('username', 'email', 'first_name', 'last_name')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields = '__all__'
        exclude = ['balance']