from django import forms

from myapp.models import projectdetail

class programForm(forms.ModelForm):
    class Meta:
        model = projectdetail
        fields = "__all__"