from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(required=True, label="Subject line", strip=True)
    email = forms.EmailField(required=True, label="Your email")
    message = forms.CharField(widget=forms.Textarea)
