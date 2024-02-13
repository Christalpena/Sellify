from django.urls import path
from .views import user_account

urlpatterns = [
    path("<str:username>/",user_account,name='userAccount')
]