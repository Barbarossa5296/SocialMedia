from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from .sitemaps import PostSitemap
from . import settings
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('temporary.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', include('comments.urls')),
    path('sitemap.xml', sitemap, {
         'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
