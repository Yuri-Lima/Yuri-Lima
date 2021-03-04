from django.contrib.sitemaps import Sitemap
from django.shortcuts import resolve_url, reverse
from .models import SendContactEmail

class EmailViewSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return ['email-contact']
    
    def location(self, item):
        return reverse(item)