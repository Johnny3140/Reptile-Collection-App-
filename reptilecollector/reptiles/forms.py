from django import forms
from .models import Reptile, Feeding

class ReptileForm(forms.ModelForm):
    class Meta:
        model = Reptile
        fields = ["name", 'species', 'color', 'size', 'description']

class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal_type', 'notes']
