from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


from .models import Store, Product, Inventory
from .forms import StoreForm, ProductForm, InventoryForm

from django.http import Http404
from django.shortcuts import get_object_or_404, redirect


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
    
    
    
class ProductListView(ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'
    
    
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

    