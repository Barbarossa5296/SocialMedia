from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'forum', views.ForumViewSet, basename='forum')

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('messages/', views.messages, name='messages'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('edit_post/<slug:slug>/',
         views.EditPost.as_view(), name='edit_post'),
    path('post/<slug:slug>/', views.ShowPost.as_view(), name='post'),
    path('api/', include(router.urls)),

]
