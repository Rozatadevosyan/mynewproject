from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog),
    path('create/', views.create),
]