from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields =["fullname" , "email","phone","resume","coverletter"]

class AtsAnalyseForm(forms.Form):
    num_to_shortlist = forms.IntegerField(label="Number of Applicants to Sortlist",min_value=1)