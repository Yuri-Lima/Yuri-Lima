from django.shortcuts import render, redirect
from django.contrib import messages
from emails.form import SendContactForm
from emails.models import SendContactEmail
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from .convertnumbers import Convert_numbers_english
from .form import NumberinWordForm

def send(request):
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
            return True
            
    else:
        messages.error(request, f'Make sure all fields are entered and valid.')
        return False

# Create your views here.
def YuriLima(request):
    if request.method =='POST':
        sended = send(request)
        if sended:
            return redirect('#contact')
        else:
            return redirect('#contact')
    else:
        email_form = SendContactForm()
    return render(request, 'yurilimacv/yurilima.html', {'email_form': email_form} )

def YuriLimaAbout(request):
    if request.method =='POST':
        sended = send(request)
        if sended:
            return redirect('#contact')
        else:
            return redirect('#contact')
    else:
        email_form = SendContactForm()
    return render(request, 'yurilimacv/yurilima.html', {'email_form': email_form} )

def YuriLimaResume(request):
    if request.method =='POST':
        sended = send(request)
        if sended:
            return redirect('#contact')
        else:
            return redirect('#contact')
    else:
        email_form = SendContactForm()
    return render(request, 'yurilimacv/yurilima.html', {'email_form': email_form} )

def YuriLimaPortofolio(request):
    if request.method =='POST':
        sended = send(request)
        if sended:
            return redirect('#contact')
        else:
            return redirect('#contact')
    else:
        email_form = SendContactForm()
    return render(request, 'yurilimacv/yurilima.html', {'email_form': email_form} )

def YuriLimaServices(request):
    if request.method =='POST':
        sended = send(request)
        if sended:
            return redirect('#contact')
        else:
            return redirect('#contact')
    else:
        email_form = SendContactForm()
    return render(request, 'yurilimacv/yurilima.html', {'email_form': email_form} )

def YuriLimaContact(request):
    if request.method =='POST':
        sended = send(request)
        if sended:
            return redirect('#contact')
        else:
            return redirect('#contact')
    else:
        email_form = SendContactForm()
    return render(request, 'yurilimacv/yurilima.html', {'email_form': email_form} )

def index_view(request):
    return render(request, 'index/index.html')

def numberinword(request):
    numbertyped = word = False
    
    if request.method =='POST':
        numbertyped = NumberinWordForm(request.POST)
        if numbertyped.is_valid():
            numbertyped_ = numbertyped.cleaned_data.get('numbertyped')
            word = Convert_numbers_english(numbertyped_)
            word.start_convertion()
            word = word.number_in_word()
    context = {
        'number': numbertyped_,
        'word' : word,
        'form' : NumberinWordForm()
    }
    # print(word.even_or_odd())
    return render(request, 'yurilimacv/portofolio/python/p1numberinword.html', context)
