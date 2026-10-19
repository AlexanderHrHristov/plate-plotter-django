from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView


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


