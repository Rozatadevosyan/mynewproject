from django.urls import path
from . import views


urlpatterns = [
    path('about', views.about),
    path('contact', views.contact),
    path('profile/', views.profile, name='profile'),
    path('', views.index),
]