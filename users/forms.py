from .models import User, Profile
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


#https://stackoverflow.com/questions/48823596/manager-isnt-available-auth-user-has-been-swapped-for-polls-user/48823691

class UserSignup(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # fields = (
        #         'username', 'first_name', 'middle_name', 'last_name', 'email',
        #          'country', 'state', 'city', 'password1', 'password2'
        #          )
        fields = ('username','first_name','last_name', 'email','password1','password2',)
        # # fields = '__all__'
        # EMAIL_FIELD = 'email'
        # USERNAME_FIELD = 'username'
        # REQUIRED_FIELDS = ['email','username']

class UserUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('first_name','last_name','username', 'email',)
        # exclude = ('password',)

class ProfileUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Profile
        fields = ('image','bio',)
