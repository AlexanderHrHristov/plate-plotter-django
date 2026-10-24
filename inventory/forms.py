from django import forms
from .models import Store, Product, Inventory

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'        


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = [
            'product',
            'available_quantity',
            'minimum_quantity',
        ]