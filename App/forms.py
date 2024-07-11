from django import forms
from App.models import PrescriptionModel


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = PrescriptionModel
        fields = ['prescription_image', 'description']

