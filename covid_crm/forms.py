from .models import User_custom
from django import forms

class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = User_custom
        fields = '__all__'
