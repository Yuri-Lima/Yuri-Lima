from django.contrib.sitemaps import Sitemap
from django.shortcuts import resolve_url, reverse


class YuriLimaCvViewSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return ['#yurilima', '#about', '#resume', '#portofolio', '#services', '#contact', '#numberinword']

    def location(self, item):
        return reverse(item)