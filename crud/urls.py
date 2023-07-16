from django.urls import path, re_path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    re_path('edit/(?P<id>\d+)', views.edit, name='edit'),
    re_path('edit/update/(?P<id>\d+)', views.update, name='update'),
    re_path('delete/(?P<id>\d+)', views.delete, name='delete'),
]