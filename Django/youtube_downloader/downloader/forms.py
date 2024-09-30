from django import forms

class DownloadForm(forms.Form):
    url = forms.URLField(label='YouTube URL', max_length=200)