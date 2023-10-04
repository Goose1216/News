from django.urls import path
from . import views

urlpatterns = [
    path('registration/signup/', views.SignUp.as_view(), name='signup')
]