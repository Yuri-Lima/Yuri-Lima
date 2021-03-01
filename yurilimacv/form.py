
from django import forms

class NumberinWordForm(forms.Form):
    numbertyped = forms.CharField(max_length=20, label='Only Numbers')
