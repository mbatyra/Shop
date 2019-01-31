# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail
from django.conf import  settings
from django.shortcuts import render
from .forms import conatactForm

# Create your views here.
def contact(request):
    title = 'Kontakt'
    form = conatactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        name = form.cleaned_data['test']
        comment = form.cleaned_data['comment']
        subject = 'Wiadomość ze sklepu'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True )
        title = "Dziękujemy!"
        confirm_message = "Dziękujemy za wiadomość, postaramy się odpisać tak szybko jak to możliwe"
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message, }
    template = 'contact.html'
    return render(request, template, context)