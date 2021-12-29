from django.contrib.sitemaps import Sitemap
from .models import Painel, Post


class PostViewSitemap(Sitemap):
    changefreq = "hourly"

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date_updated

class BoardViewSitemap(Sitemap):
    changefreq = "hourly"

    def items(self):
        return Painel.objects.all()

    def lastmod(self, obj):
        return obj.painel_date_updated