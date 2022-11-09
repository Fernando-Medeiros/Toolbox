from django.urls import path
from . import views

app_name = 'imageApp'

urlpatterns = [
    path('image/', views.home, name='home'),
]