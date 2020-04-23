from django import forms
from django.forms import CharField, Textarea


class GuestBookForm(forms.Form):
    name = CharField(label="Your name",
                     required=True,
                     strip=True)
    msg = CharField(label="Leave a message.",
                    required=True,
                    widget=Textarea(attrs={'cols': '30', 'rows': '5'}),
                    min_length=10)

