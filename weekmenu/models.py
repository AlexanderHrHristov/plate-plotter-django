from django.db import models

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

    week_menu=models.ForeignKey(
        WeekMenu, 
        on_delete=models.CASCADE,
        related_name='meals',
    )
    dish=models.ForeignKey(
        'meals.Dish',
        on_delete=models.CASCADE,
        related_name='planned_meals',
    )
    day_of_week=models.CharField(
        max_length=10,
        verbose_name='Ден от седмицата',
        choices=[
            ('Monday', 'Понеделник'),
            ('Tuesday', 'Вторник'),
            ('Wednesday', 'Сряда'),
            ('Thursday', 'Четвъртък'),
            ('Friday', 'Петък'),
            ('Saturday', 'Събота'),
            ('Sunday', 'Неделя')
        ]
    )

    meal_type=models.CharField(
        max_length=25,
        verbose_name='Тип ястие',
        choices=[
            ('Breakfast', 'Закуска'),
            ('Lunch', 'Обяд'),
            ('snack', 'Следобедна закуска'),
            ('Dinner', 'Вечеря')
        ]   
    )

    def __str__(self):
        return f"{self.name} ({self.day_of_week})"

    class Meta:
        verbose_name = 'Ястие'
        ordering = ['day_of_week']