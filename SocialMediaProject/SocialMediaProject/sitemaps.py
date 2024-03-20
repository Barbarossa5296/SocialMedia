from django.contrib.sitemaps import Sitemap
from temporary.models import Forum


class PostSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Forum.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.time_update
