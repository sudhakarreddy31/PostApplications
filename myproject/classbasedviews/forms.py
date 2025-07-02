from django import forms
from .models import Book, CBVModel

class CBVForm(forms.ModelForm):
    class Meta:
        model = CBVModel
        fields = ['title', 'description', 'is_active']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description','status', 'published_date']