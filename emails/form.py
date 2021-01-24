
from .models import SendContactEmail
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class SendContactForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = SendContactEmail
        fields = ('subject','message','from_email',)