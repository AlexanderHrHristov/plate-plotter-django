from django.urls import path

from .views import WeekMenuListView, WeekMenuCreateView,  WeekMenuDetailView, WeekMenuUpdateView, WeekMenuDeleteView 
from .views import MealCreateView, MealUpdateView, MealDeleteView, MealProductCreateView

urlpatterns = [
    path('weekmenus/',WeekMenuListView.as_view(),name='weekmenu-list'),
    path('weekmenus/add/',WeekMenuCreateView.as_view(),name='weekmenu-add'),
    path('weekmenus/<int:pk>/',WeekMenuDetailView.as_view(),name='weekmenu-detail'),
    path('weekmenus/<int:pk>/edit/',WeekMenuUpdateView.as_view(),name='weekmenu-edit'),
    path('weekmenus/<int:pk>/delete/',WeekMenuDeleteView.as_view(),name='weekmenu-delete'),
    path('weekmenus/<int:pk>/meals/add/',MealCreateView.as_view(),name='meal-add'),
    path('meals/<int:pk>/edit/',MealUpdateView.as_view(),name='meal-edit'),
    path('meals/<int:pk>/delete/',MealDeleteView.as_view(),name='meal-delete'),
    path('meals/<int:pk>/products/add/',MealProductCreateView.as_view(),name='mealproduct-add'),
]
