from .models import Post, Painel
from django.contrib import admin
from blog.forms import PostForm

@admin.register(Painel)
class PainelAdmin(admin.ModelAdmin):
    model = Painel
    fields = ('created_by','hashtag',)
    list_display = ('__str__','created_by','hashtag',)
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    fields = ('author','painel','title','slug','content_post','contact_number',)
    list_display = ('__str__','author','painel',)
    