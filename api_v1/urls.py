from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.HelloView.as_view(), name='hello'),
=======
    path('', views.CustomerCRView.as_view(),),
>>>>>>> eda7667ae57c012e262070310c09410b3faee173
    path('totalcount', views.TotalCount,),
    path('<pk>/', views.CustomerCRUDView.as_view()),
    path('userinfo', views.UserInfoListView.as_view()),
    path('api-token-auth', obtain_auth_token, name='api_token_auth'),
]
