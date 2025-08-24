from django import forms
from .models import book

class bookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ['bookname', 'author', 'category', 'Published_yr', 'About_book']