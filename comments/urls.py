from django.urls import path
from django.urls.resolvers import URLPattern
from .views import base_view , create_child_comment, create_comment

urlpatterns = [
    path('post-comments/', base_view),
    path('create-comment/', create_comment, name='comment_create'),
    path('create-child-comment/', create_child_comment, name='comment_child_create') 
]