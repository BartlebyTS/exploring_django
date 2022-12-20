from django.urls import path
from . import views

urlpatterns = [
    path('IP/', views.IP, name='IP'),
]