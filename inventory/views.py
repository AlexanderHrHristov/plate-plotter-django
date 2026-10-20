from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


from .models import Store
from .forms import StoreForm


class StoreCreateView(CreateView):
    model = Store
    form_class = StoreForm
    template_name = 'inventory/store_form.html'
    success_url = reverse_lazy('store-list')
    context_object_name = 'stores'
    

class StoreListView(ListView):
    model = Store
    template_name = 'inventory/store_list.html'
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
    


