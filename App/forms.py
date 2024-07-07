from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from App.models import PrescriptionModel


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=50,)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = PrescriptionModel
        fields = ['prescription_image', 'description']

