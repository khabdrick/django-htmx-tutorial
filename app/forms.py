from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        fields = ["name", "phone_number"]
        model = Contact