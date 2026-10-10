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