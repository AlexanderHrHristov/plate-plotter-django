from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


from .models import Store, Product, Inventory
from .forms import StoreForm, ProductForm, InventoryForm

from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.db.models import Q


class StoreListView(ListView):
    model = Store
    template_name = 'inventory/store_list.html'
    context_object_name = 'stores'   


class StoreCreateView(CreateView):
    model = Store
    form_class = StoreForm
    template_name = 'inventory/store_form.html'
    success_url = reverse_lazy('store-list')
    context_object_name = 'stores'
    

class StoreUpdateView(UpdateView):
    model = Store
    form_class = StoreForm
    template_name = 'inventory/store_form.html'
    success_url = reverse_lazy('store-list')


class StoreDeleteView(DeleteView):
    model = Store
    template_name = 'inventory/store_delete.html'
    success_url = reverse_lazy('store-list')

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request,
                'Магазинът не може да бъде изтрит, защото има '
                'свързани продукти.'
            )
            return redirect('store-list')

        messages.success(
            self.request,
            'Магазинът беше изтрит успешно.'
        )
        return response
    
    
    
class ProductListView(ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()

        search = self.request.GET.get('search', '').strip()
        category = self.request.GET.get('category', '')
        store = self.request.GET.get('store', '')
        sort = self.request.GET.get('sort', 'name')

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(brand__icontains=search)
            )

        if category:
            queryset = queryset.filter(category=category)

        if store:
            if store.isdigit():
                queryset = queryset.filter(store_id=store)

        allowed_sort_fields = ['name', '-name', 'price', '-price']

        if sort in allowed_sort_fields:
            queryset = queryset.order_by(sort)
        else:
            queryset = queryset.order_by('name')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Product.CATEGORY_CHOICES
        context['stores'] = Store.objects.all()

        context['selected_search'] = self.request.GET.get('search', '')
        context['selected_category'] = self.request.GET.get('category', '')
        context['selected_store'] = self.request.GET.get('store', '')
        context['selected_sort'] = self.request.GET.get('sort', 'name')

        return context
    
    
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product-list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product-list')
    

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'inventory/product_delete.html'
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request,
                'Продуктът не може да бъде изтрит, защото '
                'се използва в рецепта или хранене.'
            )
            return redirect('product-list')

        messages.success(
            self.request,
            'Продуктът беше изтрит успешно.'
        )
        return response


class InventoryListView(ListView):
    model = Product
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'products'


class InventoryCreateView(CreateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory-list')


class InventoryUpdateView(UpdateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory-list')

    