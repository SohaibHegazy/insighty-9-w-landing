from django.urls import path
from . import views

urlpatterns = [
    path('', views.convert_home, name='convert_home'),
]
