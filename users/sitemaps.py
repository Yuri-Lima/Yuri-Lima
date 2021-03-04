from django.contrib.sitemaps import Sitemap
from django.shortcuts import resolve_url, reverse


class UsersViewSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return ['register', 'login', 'logout', 'profile']

    def location(self, item):
        return reverse(item)