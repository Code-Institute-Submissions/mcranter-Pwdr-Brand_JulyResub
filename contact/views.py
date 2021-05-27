from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Contact Us"
            body = {
                  'first_name': form.cleaned_data['first_name'],
                  'last_name': form.cleaned_data['last_name'],
                  'email': form.cleaned_data['email_address'],
                  'message': form.cleaned_data['message'],
                  }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message,
                          'admin@pwdr.com', ['admin@pwdr.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def success(request):
    messages.success(request, 'Message sent!')
    return redirect('contact')
