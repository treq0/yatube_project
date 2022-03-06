# posts/urls.py
from django.urls import path
from . import views
app_name = 'posts'

urlpatterns = [
    path('', views.index, name='main'),
    # path('group_list.html/', views.group_posts, name='list'),
    path('group/<slug:slug>/', views.group_posts, name='list'),
]
