from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('accounts/', views.accounts, name='accounts'),
    path('post/', views.posting, name='post'),
]