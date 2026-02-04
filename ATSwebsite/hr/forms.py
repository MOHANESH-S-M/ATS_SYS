from django import forms
from .models import jobpost  # make sure jobpost model is imported

class jobpostForm(forms.ModelForm):
    class Meta:
        model = jobpost  # <-- this line is required
        fields = ["title","description","location","deadline"]
        widgets = {
            "deadline": forms.DateInput(
                attrs={"type": "date"},
                format="%Y-%m-%d"
            )
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["deadline"].input_formats = ["%Y-%m-%d"]