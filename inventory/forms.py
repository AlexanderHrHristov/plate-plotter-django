from django import forms
from .models import Store, Product, Inventory

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name']



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'brand',
            'category',
            'store',
            'unit',
            'package_quantity',
            'price',
            'is_basic',
            'calories',
            'protein',
            'carbs',
            'fat',
        ]


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = [
            'product',
            'available_quantity',
            'minimum_quantity',
        ]