from django.db import models

from decimal import Decimal
from django.core.validators import MinValueValidator


class Store(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Име',
        unique=True,
        error_messages={
        'unique': 'Вече съществува магазин с това име.'
    }
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Store'
        ordering = ['name']



class Product(models.Model):

  
    UNIT_GRAMS = 'g'
    UNIT_ML = 'ml'

    UNIT_CHOICES = [
        (UNIT_GRAMS, 'гр'),
        (UNIT_ML, 'мл')
    ]
    CATEGORY_MEAT_FISH_EGGS = 'meat_fish_eggs'
    CATEGORY_MILK_CHEESE = 'milk_cheese'
    CATEGORY_FRUIT_VEGETABLES = 'fruit_vegetables'
    CATEGORY_GRAINS = 'grains'
    CATEGORY_NUTS_OILS = 'nuts_oils'
    CATEGORY_LEGUMES = 'legumes'
    CATEGORY_SWEETS = 'sweets'
    CATEGORY_DRINKS = 'drinks'
    CATEGORY_PACKAGED_FOODS = 'packaged_foods'
    CATEGORY_SPICES = 'spices'

    CATEGORY_CHOICES = [
        (CATEGORY_MEAT_FISH_EGGS, 'Месни продукти, риба, яйца'),
        (CATEGORY_MILK_CHEESE, 'Мляко и млечни продукти'),
        (CATEGORY_FRUIT_VEGETABLES, 'Плодове и зеленчуци'),
        (CATEGORY_GRAINS, 'Хляб и зърнени продукти'),
        (CATEGORY_NUTS_OILS, 'Ядки и масла'),
        (CATEGORY_LEGUMES, 'Бобови култури и варива'),
        (CATEGORY_SWEETS, 'Сладки и десерти'),
        (CATEGORY_DRINKS, 'Напитки'),
        (CATEGORY_PACKAGED_FOODS, 'Пакетирани храни'),
        (CATEGORY_SPICES, 'Подправки')
    ]

    name = models.CharField(
        max_length=30,
        verbose_name='Продукт'
    )

    brand = models.CharField(
        max_length=30,
        verbose_name='Марка',
        blank=True
    )

    category = models.CharField(
        max_length=35,
        verbose_name='Категория',
        choices=CATEGORY_CHOICES
    )

    store = models.ForeignKey(
        Store,
        on_delete=models.PROTECT,
        verbose_name='Магазин'
    )

    unit = models.CharField(
        max_length=3,
        verbose_name='Мерна единица',
        choices=UNIT_CHOICES
    )

    package_quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name='Количество в опаковка'
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name='Цена за опаковка'
    )

 
    is_basic = models.BooleanField(
        default=False,
        verbose_name='Основен продукт',
        help_text='Базов продукт - винаги трябва да има в наличност'
    )

 
    calories = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Калории (kcal / 100 g)'
    )

    protein = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name='Протеини (g / 100 g)'
    )

    carbs = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name='Въглехидрати (g / 100 g)'
    )

    fat = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(Decimal('0'))],
        verbose_name='Мазнини (g / 100 g)'
    )


    def __str__(self):
        if self.brand:
            return f"{self.name} ({self.brand})"
        return self.name

    class Meta:
        unique_together = ('name', 'brand', 'store')
        ordering = ['name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'



class Inventory(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    
    available_quantity = models.PositiveIntegerField(
        verbose_name='Налично количество',
        blank=True,
        default=0
    )
    


    minimum_quantity = models.PositiveIntegerField(
        verbose_name='Минимално количество',
        blank=True,
        default=0
    )
    
    
    def __str__(self):
        return f"{self.product.name} - {self.product.brand} - {self.available_quantity} {self.product.unit}"
    
    def is_product_below_minimum(self):
        return self.available_quantity < self.minimum_quantity
    