from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    email_address = forms.EmailField(max_length=120)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
