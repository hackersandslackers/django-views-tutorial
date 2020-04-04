from django import forms


class GuestBookForm(forms.Form):
    name = forms.CharField(required=True, label="Your name", strip=True)
    message = forms.CharField(required=True, label="Your message to the world", strip=True)
