from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm,UserChangeForm, PasswordResetForm
#https://stackoverflow.com/questions/48823596/manager-isnt-available-auth-user-has-been-swapped-for-polls-user/48823691

class UserSignup(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','first_name','last_name','password1','password2',)
        REQUIRED_FIELDS = ['username','first_name','last_name']

class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = ("This E-Mail address is not registered.")
            self.add_error('email', msg)
        return email

class UserUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('first_name','last_name','username', 'email',)

class ProfileUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Profile
        fields = ('image','bio',)
