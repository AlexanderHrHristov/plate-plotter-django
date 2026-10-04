from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Store"
        ordering = ['name']


class Product(models.Model):
    class CategoryChoices(models.TextChoices):
        FRUITS = 'fruits', 'Fruits'
        VEGETABLES = 'vegetables', 'Vegetables'
        MEAT = 'meat', 'Meat'
        FISH = 'fish', 'Fish'
        DAIRY = 'dairy', 'Dairy'
        BAKERY = 'bakery', 'Bakery'
        BEVERAGES = 'beverages', 'Beverages'
        SNACKS = 'snacks', 'Snacks'
        NUTS_SEEDS = 'nuts', 'Nuts & Seeds'
        FROZEN = 'frozen', 'Frozen'
        SPICES = 'spices', 'Spices'
        PASTA_RICE = 'pasta_rice', 'Pasta & Rice'
        BREAKFAST_CEREALS = 'cereals', 'Breakfast Cereals'
        SWEETS_DESSERTS = 'sweets', 'Sweets & Desserts'
        OTHER = 'other', 'Other'

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30, choices=CategoryChoices.choices)
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        ordering = ['name']