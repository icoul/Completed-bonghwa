from django import forms

class UploadFileForm(forms.Form):
    content = forms.CharField(max_length=150)
    image = forms.FileField(required=False)
    mentionIndex = forms.IntegerField(required=False)
    mentionDepth = forms.IntegerField(required=False)
