from django.urls import path
from .views import StoreCreateView, StoreListView, StoreUpdateView, StoreDeleteView
from .views import ProductCreateView, ProductListView, ProductUpdateView, ProductDeleteView
from .views import InventoryListView, InventoryCreateView, InventoryUpdateView



urlpatterns = [
    path('stores/', StoreListView.as_view(), name='store-list'),
    path('stores/add/', StoreCreateView.as_view(), name='store-add'),
    path('stores/<int:pk>/edit/', StoreUpdateView.as_view(), name='store-edit'),
    path('stores/<int:pk>/delete/', StoreDeleteView.as_view(), name='store-delete'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/add/', ProductCreateView.as_view(), name='product-add'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product-edit'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('inventory/', InventoryListView.as_view(), name='inventory-list'),
    path('inventory/add/', InventoryCreateView.as_view(), name='inventory-add'),
    path('inventory/<int:pk>/edit/', InventoryUpdateView.as_view(), name='inventory-edit'),
]