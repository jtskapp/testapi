from django.urls import path

from . import views

urlpatterns = [
    path('', views.CustomerCRView.as_view(),),
    path('<pk>/', views.CustomerCRUDView.as_view()),
]