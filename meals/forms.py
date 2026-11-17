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
        labels = {
            'product': 'Продукт',
            'quantity': 'Количество',
        }
        widgets = {
            "quantity": forms.NumberInput(
                attrs={"placeholder": "Въведете количество"}
            ),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["product"].empty_label = "Изберете продукт"


RecipeItemFormSet = inlineformset_factory(
    Dish,
    RecipeItem,
    form=RecipeItemForm,
    extra=1,
    can_delete=True,
)