from django.urls import path
from . import views

#those imports that are below are for seeing imgs in the admin panel
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Feed_redirect, name='Feed_redirect'),
    path('feed/', views.Feed, name='Feed'),
]

urlpatterns += static(settings.MEDIA_URL, document_root =  settings.MEDIA_ROOT)