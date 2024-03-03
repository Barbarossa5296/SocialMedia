from django.urls import path
from .views import AddComment

app_name = 'comments'


urlpatterns = [
    path('post/<slug:slug>/add_comment/', AddComment.as_view(),
         name='add_comment_to_post'),
]
