from django import forms
from django.forms import CharField, Textarea, IntegerField


class GuestBookForm(forms.Form):
    name = CharField(label="Your name",
                     required=True,
                     strip=True)
    msg = CharField(label="Leave a message.",
                    required=True,
                    widget=Textarea(attrs={'cols': '30', 'rows': '5'}),
                    min_length=10)


class ViewUserProfile(forms.Form):
    id = IntegerField(required=True,
                      label="Enter an ID.")
