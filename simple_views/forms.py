from django import forms


class GuestBookForm(forms.Form):
    name = forms.CharField(required=True,
                           label="Your name",
                           strip=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': '30', 'rows': '10'}),
                              required=True,
                              label="Leave a message!")


class ViewUserProfile(forms.Form):
    id = forms.IntegerField(required=True,
                            label="Enter an ID to test `get_or_404()` logic.")
