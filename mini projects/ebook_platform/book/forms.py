from django import forms
from .models import Ebook, Poster, BusinessCard

class EbookForm(forms.ModelForm):
    class Meta:
        model = Ebook
        fields = ['title', 'author', 'file']

class PosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = ['title', 'image']

class BusinessCardForm(forms.ModelForm):
    class Meta:
        model = BusinessCard
        fields = ['name', 'email', 'phone', 'image']
