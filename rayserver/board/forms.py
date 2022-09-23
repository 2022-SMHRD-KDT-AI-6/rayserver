from django import forms
from .models import Writing
class WritingFrom(forms.ModelForm):
    class Meta:
        model = Writing
        fields = ['Subject', 'content']