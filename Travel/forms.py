from django import forms

class ContactForm(forms.Form):
    name    = forms.CharField()
    email   = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':10}))