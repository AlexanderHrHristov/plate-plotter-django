from django.urls import path
from .views import StoreCreateView, StoreListView

urlpatterns = [
    path('stores/', StoreListView.as_view(), name='store-list'),
    path('stores/add/', StoreCreateView.as_view(), name='store-add'),
]