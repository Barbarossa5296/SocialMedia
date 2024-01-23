from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('messages/', views.messages, name='messages'),
    path('forum/', views.AddPost.as_view(), name='forum'),

]
