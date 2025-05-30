from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields =["fullname" , "email","phone","resume","coverletter"]
