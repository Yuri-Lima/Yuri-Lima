
from .models import SendContactEmail
from django import forms

class SendContactForm(forms.ModelForm):
    class Meta:
        model = SendContactEmail
        fields = ('subject','message','from_email',)