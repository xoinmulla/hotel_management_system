from django import forms
from .models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score', 'comment']
        widgets = {
            'score': forms.NumberInput(attrs={'min': 1, 'max': 5}),  # Allow ratings from 1 to 5
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
