from django.db import models

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
    quantity = models.DecimalField(
        max_digits=10, 
        decimal_places=2
        )

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
