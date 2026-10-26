from django.db import models

from decimal import Decimal

class Dish(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True
        )
    description = models.TextField(
        blank=True
        )
    preparation_time = models.PositiveIntegerField(
        verbose_name='Време за приготвяне (в минути)',
        blank=True,
        null=True
    )
    servings = models.PositiveIntegerField(
        verbose_name='Bрой порции',
        default=1
    )
    
        
    products = models.ManyToManyField(
        'inventory.Product', 
        through='RecipeItem',
        related_name='dishes'
        )

    def __str__(self):
        return self.name
    
    def calculate_macros(self):
        if not self.recipe_items.exists():
            return None
        
        totals = {
            'calories': Decimal('0'),
            'protein': Decimal('0'),
            'carbs': Decimal('0'),
            'fat': Decimal('0'),
        }

        for item in self.recipe_items.select_related('product'):
            product = item.product

            if product.unit != 'g':
                return None
            values = (
                product.calories,
                product.protein,
                product.carbs,
                product.fat,
            )

            if any(value is None for value in values):
                return None

            factor = item.quantity / Decimal('100')

            totals['calories'] += Decimal(product.calories) * factor
            totals['protein'] += product.protein * factor
            totals['carbs'] += product.carbs * factor
            totals['fat'] += product.fat * factor

        if self.servings == 0:
            return None

        return {
            key: round(value / self.servings, 1)
            for key, value in totals.items()
        }

    class Meta:
        verbose_name = 'Ястие'
        ordering = ['name']


class RecipeItem(models.Model):
    dish = models.ForeignKey(
        Dish, 
        on_delete=models.CASCADE, 
        related_name='recipe_items'
        )
    product = models.ForeignKey(
        'inventory.Product', 
        on_delete=models.PROTECT,
        )
    quantity = models.PositiveIntegerField()
    

    def __str__(self):
        return f"{self.quantity} of {self.product.name} for {self.dish.name}"

    class Meta:
        verbose_name = 'Продукт в рецептата'
        ordering = ['dish', 'product']
        constraints = [
            models.UniqueConstraint(
                fields=['dish', 'product'], 
                name='unique_product_per_dish'
            )
        ]
