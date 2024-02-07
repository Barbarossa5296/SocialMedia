from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('messages/', views.messages, name='messages'),
    path('forum/', views.AddPost.as_view(), name='forum'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),


]
