from django import forms
from .models import *

class EmergencyForm(forms.ModelForm):
    class Meta:
        model = Emergency
        exclude = [""]

class EmergencyImageForm(forms.ModelForm):
    class Meta:
        model = EmergencyImage
        fields = ('image',)