
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(
        pattern_name='store-list',
        permanent=False
    )),
    path('', include('inventory.urls')),
    path('', include('meals.urls')),
]