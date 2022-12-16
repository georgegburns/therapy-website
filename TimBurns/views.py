from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.core.mail import send_mail
from . import forms
from . import models


def view_404(request, exception=None):
    return redirect('index')

def index(request):
    if request.method == 'POST':
        form = forms.MessageForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('Name')
            therapy = form.cleaned_data.get('Therapy')
            ftype = form.cleaned_data.get('Type')
            email = form.cleaned_data.get('Email')
            subject = f'{name} - {therapy} - {ftype} - {email}'
            message = form.cleaned_data.get('Message')
            send_mail(
                subject = subject,
                message = message,
                from_email = 'drtimburnstherapy@gmail.com',
                recipient_list= ['drtimburnstherapy@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, ('You\'ll hear from us soon!'))
        else:
            messages.error(request, ('Your message didn\'t send, please try again.'))
        return redirect('index')
    context = {}
    context['prices'] = models.Prices.objects.all().order_by('Therapy')
    context['messageform'] = forms.MessageForm
    return render(request, 'index.html', context)

def landing(request):
    context = {}
    return render(request, 'landing.html', context)