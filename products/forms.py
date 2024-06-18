from django import forms
from .models import Product, Comment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price'] # , 'cover']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'recommend']
