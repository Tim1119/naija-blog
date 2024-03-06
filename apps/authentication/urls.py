from django.contrib import admin
from django.urls import path, include
from .views import RegistrationView, LoginUser, UserLogoutView

app_name = 'authentication'


urlpatterns = [
    path('', RegistrationView.as_view(), name='registration'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', UserLogoutView, name='logout'),
]

