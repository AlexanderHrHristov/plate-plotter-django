from django import forms

from .models import WeekMenu, Meal,MealProduct


class WeekMenuForm(forms.ModelForm):
    class Meta:
        model = WeekMenu
        fields = ['name', 'start_date']

        labels = {
            'name': 'Име на менюто',
            'start_date': 'Начална дата',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'start_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                },
                format='%Y-%m-%d'
            ),
        }


    
class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['day_of_week', 'meal_type', 'dish']
        
        labels = {
            'day_of_week': 'Ден от седмицата',
            'meal_type': 'Хранене',
            'dish': 'Ястие',
        }

        widgets = {
            'day_of_week': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'meal_type': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'dish': forms.Select(
                attrs={'class': 'form-select'}
            ),
        }


class MealProductForm(forms.ModelForm):
    class Meta:
        model = MealProduct
        fields = ['product', 'quantity']