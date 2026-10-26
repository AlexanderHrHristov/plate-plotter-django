from django import forms
from django.forms import inlineformset_factory

from .models import Dish, RecipeItem


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = [
            'name',
            'description',
            'preparation_time',
            'servings',
        ]


class RecipeItemForm(forms.ModelForm):
    class Meta:
        model = RecipeItem
        fields = ['product', 'quantity']


RecipeItemFormSet = inlineformset_factory(
    Dish,
    RecipeItem,
    form=RecipeItemForm,
    extra=1,
    can_delete=True,
)