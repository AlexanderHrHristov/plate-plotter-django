from django.urls import path
from .views import DishListView, DishCreateView, DishUpdateView, DishDeleteView, RecipeItemDeleteView, RecipeItemUpdateView
from .views import RecipeItemCreateView, DishDetailView

urlpatterns = [
    path('dishes/', DishListView.as_view(), name='dish-list'),
    path('dishes/add/', DishCreateView.as_view(), name='dish-add'),
    path('dishes/<int:pk>/edit/', DishUpdateView.as_view(), name='dish-edit'),
    path('dishes/<int:pk>/delete/', DishDeleteView.as_view(), name='dish-delete'),
    path('dishes/<int:pk>/recipe-items/add/', RecipeItemCreateView.as_view(), name='recipeitem-add'),
    path('dishes/<int:pk>/', DishDetailView.as_view(), name='dish-detail'),
    path('ingredients/<int:pk>/edit/',RecipeItemUpdateView.as_view(),name='recipeitem-edit'),
    path('ingredients/<int:pk>/delete/',RecipeItemDeleteView.as_view(),name='recipeitem-delete'),
]   