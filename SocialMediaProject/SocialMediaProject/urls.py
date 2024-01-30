from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('temporary.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('social-auth/', include('social_django.urls', namespace='social')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
