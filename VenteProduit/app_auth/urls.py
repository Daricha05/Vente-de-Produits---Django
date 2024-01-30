from django.urls import path
from .views import Register, Login, Logout


urlpatterns = [
    path('', Login, name='login'),
    path('register/', Register, name='register'),
    path('logout/', Logout, name='logout'),
]
