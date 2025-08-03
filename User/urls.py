from django import urls
from django.urls import path
from .views import *
app_name = 'user'
urlpatterns = [
    path('', views_login, name = 'login'),
    path('index/', views_index, name = 'index'),
    path('register/', views_user_registration, name = 'register'),
    path('logout/', views_logout, name = 'logout'),
    path('home/', views_home, name = 'home'),  
    path('Change_Password/', view_passwordChange.as_view(), name='Change_Password'),    
    path('password_reset/', view_passwordReset.as_view(), name='password_reset'),  
]