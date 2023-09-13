from django.urls import path
from . import views

urlpatterns = [
    path('',views.login),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
    path('index', views.index, name='index')
]
