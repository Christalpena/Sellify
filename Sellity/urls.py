from django.urls import path
from . import views

urlpatterns = [
    path('', views.Feed_redirect, name='Feed_redirect'),
    path('feed/', views.Feed, name='Feed'),
]