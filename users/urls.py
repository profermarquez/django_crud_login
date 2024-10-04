from django.urls import path
from .views import home, profile, RegisterView
from django.urls import include

urlpatterns = [
    #path('', home, name='users-home'),
    path('', include('productos.urls')),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
]
