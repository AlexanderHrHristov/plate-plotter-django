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
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Напр. Пилешко филе'
            }),
            'brand': forms.TextInput(attrs={
                'placeholder': 'Напр. Lidl'
            }),
            'package_quantity': forms.NumberInput(attrs={
                'placeholder': 'Напр. 500',
                'min': 1
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Напр. 8.99',
                'min': 0.01,
                'step': 0.01
            }),
            'calories': forms.NumberInput(attrs={
                'placeholder': 'kcal за 100 г'
            }),
            'protein': forms.NumberInput(attrs={
                'placeholder': 'Протеини за 100 г'
            }),
            'carbs': forms.NumberInput(attrs={
                'placeholder': 'Въглехидрати за 100 г'
            }),
            'fat': forms.NumberInput(attrs={
                'placeholder': 'Мазнини за 100 г'
            }),
        }

        help_texts = {
            'package_quantity': 'Количество в една опаковка според избраната мерна единица.',
            'price': 'Цена за цялата опаковка.',
            'calories': 'Енергийна стойност за 100 г продукт.',
            'protein': 'Протеини в грамове за 100 г продукт.',
            'carbs': 'Въглехидрати в грамове за 100 г продукт.',
            'fat': 'Мазнини в грамове за 100 г продукт.',
        }

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = [
            'product',
            'available_quantity',
            'minimum_quantity',
        ]