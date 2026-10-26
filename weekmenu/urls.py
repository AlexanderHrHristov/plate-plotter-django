
from django.urls import path

from .views import WeekMenuListView, WeekMenuCreateView,  WeekMenuDetailView


urlpatterns = [
    path('weekmenus/',WeekMenuListView.as_view(),name='weekmenu-list'),
    path('weekmenus/add/',WeekMenuCreateView.as_view(),name='weekmenu-add'),
    path('weekmenus/<int:pk>/',WeekMenuDetailView.as_view(),name='weekmenu-detail'
),
]
