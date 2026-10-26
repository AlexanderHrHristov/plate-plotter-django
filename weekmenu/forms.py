
from django import forms

from .models import WeekMenu
from django.views.generic import DetailView, ListView, CreateView

class WeekMenuForm(forms.ModelForm):
    class Meta:
        model = WeekMenu
        fields = ['name', 'start_date']

        labels = {
            'name': 'Име на менюто',
            'start_date': 'Начална дата',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'start_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                },
                format='%Y-%m-%d'
            ),
        }


class WeekMenuDetailView(DetailView):
    model = WeekMenu
    template_name = 'weekmenu/weekmenu_detail.html'
    context_object_name = 'week_menu'