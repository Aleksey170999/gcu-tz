from django import forms

from apps.catalog.models import Product, Category


class CategoryCreateForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['title', 'manager']


class ProductCreateForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category']