from django import forms
from .models import Contact, Resume, PDFFile

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file', 'description']

class PDFFileForm(forms.ModelForm):
    class Meta:
        model = PDFFile
        fields = ['title', 'file']
