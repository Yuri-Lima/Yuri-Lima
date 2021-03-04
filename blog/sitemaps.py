from django.contrib import sitemaps
from django.contrib.sitemaps import Sitemap
from django.shortcuts import resolve_url, reverse
from .models import Painel, Post


class PostViewSitemap(Sitemap):

    def items(self):
        return Post.objects.all()

    # def location(self, item):
    #     return reverse(item)

class BoardViewSitemap(Sitemap):

    def items(self):
        return Painel.objects.all()