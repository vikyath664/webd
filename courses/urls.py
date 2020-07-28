from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.timepass, name='timepass'),
    path('postlogin/', views.postloginin, name='postlogin'),
    path('postsignup/', views.postsignup, name='postsignup'),
    url(r'^logout/',views.logout,name="log")
]
