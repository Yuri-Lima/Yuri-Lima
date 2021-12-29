from django.shortcuts import render, redirect
from django.contrib import messages
from .form import SendContactForm
from .models import SendContactEmail
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def send_email(request):
    if request.method =='POST':
        email_form = SendContactForm(request.POST)#,instance=request.user
        if email_form.is_valid():
            email_form.save()
            subject = email_form.cleaned_data.get('subject')
            # print('Subject:',subject)
            message = email_form.cleaned_data.get('message')
            # print('Message:',message)
            from_email = email_form.cleaned_data.get('from_email')
            # print('From_email:',from_email)
            to_email = 'y.m.lima19@gmail.com'
            if subject and message and from_email:
                try:
                    send_mail(subject, message, from_email, [to_email], fail_silently=False,)

                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

                messages.success(request, f'Your email has been submited!'),
                return redirect('painel-list')
        else:
            messages.error(request, f'Make sure all fields are entered and valid.')
            return redirect('email-contact')
    else:
        email_form = SendContactForm()
    return render(request,'email/contact.html', {'email_form': email_form})