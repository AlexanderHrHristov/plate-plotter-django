from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Dish, RecipeItem
from django.urls import reverse_lazy
from .forms import DishForm, RecipeItemForm, RecipeItemFormSet
from django.http import HttpResponseRedirect    
from django.db import transaction


class DishListView(ListView):
    model = Dish
    template_name = 'meals/dish_list.html'
    context_object_name = 'dishes'


from django.db import transaction


class DishCreateView(CreateView):
    model = Dish
    form_class = DishForm
    template_name = 'meals/dish_form.html'
    success_url = reverse_lazy('dish-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'formset' not in context:
            if self.request.method == 'POST':
                context['formset'] = RecipeItemFormSet(self.request.POST)
            else:
                context['formset'] = RecipeItemFormSet()

        return context

    def form_valid(self, form):
        formset = RecipeItemFormSet(self.request.POST)

        if not formset.is_valid():
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )

        with transaction.atomic():
            self.object = form.save()
            formset.instance = self.object
            formset.save()

        return super(CreateView, self).form_valid(form)
    

class DishUpdateView(UpdateView):
    model = Dish
    form_class = DishForm
    template_name = 'meals/dish_form.html'
    success_url = reverse_lazy('dish-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'formset' not in context:
            if self.request.method == 'POST':
                context['formset'] = RecipeItemFormSet(
                    self.request.POST,
                    instance=self.object
                )
            else:
                context['formset'] = RecipeItemFormSet(
                    instance=self.object
                )

        return context

    def form_valid(self, form):
        formset = RecipeItemFormSet(
            self.request.POST,
            instance=self.object
        )

        if not formset.is_valid():
            return self.render_to_response(
                self.get_context_data(
                    form=form,
                    formset=formset
                )
            )

        with transaction.atomic():
            self.object = form.save()
            formset.instance = self.object
            formset.save()

        return HttpResponseRedirect(self.get_success_url())

class DishDeleteView(DeleteView):
    model = Dish
    template_name = 'meals/dish_delete.html'
    success_url = reverse_lazy('dish-list')


class DishDetailView(DetailView):
    model = Dish
    template_name = 'meals/dish_detail.html'
    context_object_name = 'dish'


class RecipeItemCreateView(CreateView):
    model = RecipeItem
    form_class = RecipeItemForm
    template_name = 'meals/recipeitem_form.html'
    def get_success_url(self):
        return reverse_lazy('dish-detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        dish_id = self.kwargs['pk']
        product = form.cleaned_data['product']

        if RecipeItem.objects.filter(
            dish_id=dish_id,
            product=product
        ).exists():
            form.add_error(
                'product',
                'Този продукт вече е добавен към ястието.'
            )
            return self.form_invalid(form)

        form.instance.dish_id = dish_id
        return super().form_valid(form)


class RecipeItemUpdateView(UpdateView):
    model = RecipeItem
    form_class = RecipeItemForm
    template_name = 'meals/recipeitem_form.html'

    def get_success_url(self):
        return reverse_lazy('dish-detail', kwargs={'pk': self.object.dish.pk})



class RecipeItemDeleteView(DeleteView):
    model = RecipeItem
    template_name = 'meals/recipeitem_delete.html'

    def get_success_url(self):
        return reverse_lazy('dish-detail', kwargs={'pk': self.object.dish.pk})