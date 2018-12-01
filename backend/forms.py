from django import forms

class UploadFileForm(forms.Form):
    contents = forms.CharField(max_length=150)
    file = forms.FileField(required=False)
