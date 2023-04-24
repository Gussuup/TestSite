from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('second', views.about),
    path('create', views.create, name='create')
]