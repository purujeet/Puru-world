from django import forms
from .models import feedback

class feedbackform(forms.Form):
    ftopic = forms.TextInput()
    fques = forms.TextInput()
    fans = forms.Textarea()

