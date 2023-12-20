from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('comrades/', views.comrades, name='comrades'),
    path('messages/', views.messages, name='messages'),
    path('forum/', views.forum, name='forum'),

]
