from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import WeekMenu, Meal
from .forms import WeekMenuForm, MealForm, MealProductForm, MealProduct


from django.shortcuts import get_object_or_404

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
    
    
    
class WeekMenuUpdateView(UpdateView):
    model = WeekMenu
    form_class = WeekMenuForm
    template_name = 'weekmenu/weekmenu_form.html'
    success_url = reverse_lazy('weekmenu-list')



class WeekMenuDeleteView(DeleteView):
    model = WeekMenu
    template_name = 'weekmenu/weekmenu_delete.html'
    success_url = reverse_lazy('weekmenu-list')
    
    


class MealCreateView(CreateView):
    model = Meal
    form_class = MealForm
    template_name = 'weekmenu/meal_form.html'

    def form_valid(self, form):
        form.instance.week_menu_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'weekmenu-detail',
            kwargs={'pk': self.kwargs['pk']}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['week_menu'] = get_object_or_404(
            WeekMenu,
            pk=self.kwargs['pk']
        )
        return context
    
    
    
class MealUpdateView(UpdateView):
    model = Meal
    form_class = MealForm
    template_name = 'weekmenu/meal_form.html'

    def get_success_url(self):
        return reverse_lazy(
            'weekmenu-detail',
            kwargs={'pk': self.object.week_menu_id}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['week_menu'] = self.object.week_menu
        return context


class MealDeleteView(DeleteView):
    model = Meal
    template_name = 'weekmenu/meal_delete.html'

    def get_success_url(self):
        return reverse_lazy(
            'weekmenu-detail',
            kwargs={'pk': self.object.week_menu_id}
        )


class MealProductCreateView(CreateView):
    model = MealProduct
    form_class = MealProductForm
    template_name = 'weekmenu/mealproduct_form.html'

    def form_valid(self, form):
        meal = get_object_or_404(
            Meal,
            pk=self.kwargs['pk']
        )

        product = form.cleaned_data['product']

        if MealProduct.objects.filter(
            meal=meal,
            product=product
        ).exists():
            form.add_error(
                'product',
                'Този продукт вече е добавен към храненето.'
            )
            return self.form_invalid(form)

        form.instance.meal = meal
        return super().form_valid(form)

    def get_success_url(self):
        meal = get_object_or_404(
            Meal,
            pk=self.kwargs['pk']
        )

        return reverse_lazy(
            'weekmenu-detail',
            kwargs={'pk': meal.week_menu_id}
        )
