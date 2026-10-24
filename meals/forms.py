from django import forms
from .models import Dish, RecipeItem

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'preparation_time', 'servings']

class RecipeItemForm(forms.ModelForm):
    class Meta:
        model = RecipeItem
        fields = ['product', 'quantity']