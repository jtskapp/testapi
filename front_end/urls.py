from django.urls import path
from django.conf.urls import url, include
from front_end import views

urlpatterns = [
    path('', views.index, name='index'),
    path('navbar/', views.navbar, name='navbar'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('element/', views.element, name='element'),
    path('tables/', views.tables, name='tables'),
    path('bs4/', views.Bs4.as_view(), name='bs4'),
]
