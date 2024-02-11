from django.urls import path
from .views import SignUp,CompleteProfile

urlpatterns = [
    path("signup/",SignUp.as_view(),name='signUp'),
    path('complete-profile/',CompleteProfile.as_view(), name='complete_profile')
]