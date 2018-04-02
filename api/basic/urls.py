from django.urls import path, include
from basic import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.app_login),
    path('register', views.app_register),
    path('logout', views.app_logout),
    path('get_posts', views.get_posts),
    path('get_post_by_title', views.get_post_by_title),
    path('get_user_by_username', views.get_user_by_username),
    path('get_system_mesg_by_username', views.get_system_mesg_by_username),
]
