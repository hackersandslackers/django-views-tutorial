from django import forms


class UserForm(forms.Form):
    name = forms.CharField(required=True, label="Search for username.", strip=True)
