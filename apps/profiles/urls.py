from django.urls import path, include
from .views import ProfileListView,UpdateProfileView

app_name = 'profile'


urlpatterns = [

    path('',ProfileListView.as_view(), name='profile'),
    path('update-profile/<str:slug>/',UpdateProfileView.as_view(), name='update-profile'),
  
]
