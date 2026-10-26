from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .models import WeekMenu
from .forms import WeekMenuForm


class WeekMenuListView(ListView):
    model = WeekMenu
    template_name = 'weekmenu/weekmenu_list.html'
    context_object_name = 'week_menus'


class WeekMenuCreateView(CreateView):
    model = WeekMenu
    form_class = WeekMenuForm
    template_name = 'weekmenu/weekmenu_form.html'
    success_url = reverse_lazy('weekmenu-list')


class WeekMenuDetailView(DetailView):
    model = WeekMenu
    template_name = 'weekmenu/weekmenu_detail.html'
    context_object_name = 'week_menu'