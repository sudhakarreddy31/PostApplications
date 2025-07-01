from django import forms
from .models import CBVModel

class CBVForm(forms.ModelForm):
    class Meta:
        model = CBVModel
        fields = ['title', 'description', 'is_active']
