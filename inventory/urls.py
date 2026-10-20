from django.urls import path
from .views import StoreCreateView, StoreListView, StoreUpdateView, StoreDeleteView

urlpatterns = [
    path('stores/', StoreListView.as_view(), name='store-list'),
    path('stores/add/', StoreCreateView.as_view(), name='store-add'),
    path('stores/<int:pk>/edit/', StoreUpdateView.as_view(), name='store-edit'),
    path('stores/<int:pk>/delete/', StoreDeleteView.as_view(), name='store-delete'),
]