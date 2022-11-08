from django.urls import path
from . import views

app_name = 'downloadApp'


urlpatterns = [
    path('videodownload/', views.home, name='home'),
]