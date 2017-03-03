from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)