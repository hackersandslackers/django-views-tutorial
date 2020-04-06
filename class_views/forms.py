from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label="Your name", strip=True)
    email = forms.EmailField(required=True, label="Your email")
    message = forms.CharField(widget=forms.Textarea)
