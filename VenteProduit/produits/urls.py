from django.urls import path
from .views import Home, detail


urlpatterns = [
    path('', Home, name='homeProduct'),
    path('detail/<str:id>', detail, name='detailProduct'),
]
