from django.db import models

from decimal import Decimal

class WeekMenu(models.Model):
    name=models.CharField(
        max_length=100, 
        unique=True
        )
    start_date=models.DateField(
        verbose_name='Начална дата на седмичното меню',
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Седмично меню'
        ordering = ['-start_date']



class Meal(models.Model):

    week_menu = models.ForeignKey(
        WeekMenu,
        on_delete=models.CASCADE,
        related_name='meals',
    )

    dish = models.ForeignKey(
        'meals.Dish',
        on_delete=models.CASCADE,
        related_name='planned_meals',
        blank=True,
        null=True,
    )

    day_of_week = models.CharField(
        max_length=10,
        verbose_name='Ден от седмицата',
        choices=[
            ('Monday', 'Понеделник'),
            ('Tuesday', 'Вторник'),
            ('Wednesday', 'Сряда'),
            ('Thursday', 'Четвъртък'),
            ('Friday', 'Петък'),
            ('Saturday', 'Събота'),
            ('Sunday', 'Неделя'),
        ]
    )

    meal_type = models.CharField(
        max_length=25,
        verbose_name='Тип ястие',
        choices=[
            ('Breakfast', 'Закуска'),
            ('Lunch', 'Обяд'),
            ('snack', 'Следобедна закуска'),
            ('Dinner', 'Вечеря'),
        ]
    )

    def calculate_macros(self):
        totals = {
            'calories': Decimal('0'),
            'protein': Decimal('0'),
            'carbs': Decimal('0'),
            'fat': Decimal('0'),
        }

        if self.dish:
            dish_macros = self.dish.calculate_macros()

            if dish_macros is None:
                return None

            for key in totals:
                totals[key] += dish_macros[key]

        meal_products = self.products.select_related('product')

        if not self.dish and not meal_products.exists():
            return None

        for item in meal_products:
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

            factor = Decimal(item.quantity) / Decimal('100')

            totals['calories'] += Decimal(product.calories) * factor
            totals['protein'] += product.protein * factor
            totals['carbs'] += product.carbs * factor
            totals['fat'] += product.fat * factor

        return {
            key: round(value, 1)
            for key, value in totals.items()
        }

    def __str__(self):
        dish_name = self.dish.name if self.dish else "Без ястие"

        return (
            f"{dish_name} "
            f"({self.get_day_of_week_display()} - "
            f"{self.get_meal_type_display()})"
        )

    class Meta:
        verbose_name = 'Планирано хранене'
        verbose_name_plural = 'Планирани хранения'
        ordering = [
        models.Case(
        models.When(day_of_week='Monday', then=models.Value(1)),
        models.When(day_of_week='Tuesday', then=models.Value(2)),
        models.When(day_of_week='Wednesday', then=models.Value(3)),
        models.When(day_of_week='Thursday', then=models.Value(4)),
        models.When(day_of_week='Friday', then=models.Value(5)),
        models.When(day_of_week='Saturday', then=models.Value(6)),
        models.When(day_of_week='Sunday', then=models.Value(7)),
        default=models.Value(8),
        output_field=models.IntegerField(),
    ),
    'meal_type',
]


class MealProduct(models.Model):
    meal = models.ForeignKey(
        Meal,
        on_delete=models.CASCADE,
        related_name='products',
    )

    product = models.ForeignKey(
        'inventory.Product',
        on_delete=models.PROTECT,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Количество',
    )

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

    class Meta:
        verbose_name = 'Продукт в хранене'
        verbose_name_plural = 'Продукти в хранене'
        constraints = [
            models.UniqueConstraint(
                fields=['meal', 'product'],
                name='unique_product_per_meal',
            )
        ]
