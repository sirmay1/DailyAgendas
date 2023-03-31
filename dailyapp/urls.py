from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('journal/', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('account/', views.useraccount, name='useraccount'),
    path('post/', views.posting, name='post'),
]