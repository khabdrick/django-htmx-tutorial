from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        fields = ["name", "tips"]
        model = Contact
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
        }