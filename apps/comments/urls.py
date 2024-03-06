from django.urls import path, include
from .views import comment_create_view,comment_delete_view
app_name = 'comments'


urlpatterns = [

    path('', comment_create_view, name='create-comment'),
    path('delete-comment/', comment_delete_view, name='delete-comment'),

]
