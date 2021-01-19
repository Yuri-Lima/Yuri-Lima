from django.shortcuts import render, redirect
from .forms import UserSignup, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, get_user
from django.conf import settings


# Create your views here.

#https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/
def register(request):
    if request.method =='POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Thanks {username}! Now You are able to Login')
            return redirect('login')
        else:
            messages.error(request, f'Something Went Wrong, Try Again')
            return redirect('register')
    else:
        form = UserSignup()
    return render(request,'users/register.html',{'form': form})

@login_required
def profile(request):#https://www.youtube.com/watch?v=CQ90L5jfldw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=9
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)#request.FILES, 
        if u_form.is_valid():
            u_form.save()
            if p_form.is_valid():
                p_form.save()
                messages.success(request, f'Your account has beend updated!')
                return redirect('profile')
        else:
            messages.error(request, f'Something Went Wrong, Try update it Again')
            return redirect('profile')
    else:
        
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    fullname = request.user.get_full_name() #https://stackoverflow.com/questions/41153052/get-fullname-of-user-from-django-user-model
    context = {
        'u_form':u_form, 
        'p_form':p_form,
        'fullname':fullname
    }
    return render(request, 'users/profile.html', context)




# messages.debug
# messages.info
# messages.success
# messages.warnig
# messages.error