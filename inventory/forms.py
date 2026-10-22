from django import forms
from .models import Store, Product

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'        
    