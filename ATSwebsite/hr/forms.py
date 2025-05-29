from django import forms
from .models import jobpost  # make sure jobpost model is imported

class jobpostForm(forms.ModelForm):
    class Meta:
        model = jobpost  # <-- this line is required
        fields = ["title","description","location","deadline"]
