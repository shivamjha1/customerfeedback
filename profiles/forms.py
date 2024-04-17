from django import forms

class FileForm(forms.Form):
    file=forms.ImageField()