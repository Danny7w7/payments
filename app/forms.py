import datetime
from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
        exclude = ['company', 'date_joined']