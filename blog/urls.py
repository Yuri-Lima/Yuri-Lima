
from django.urls import path
from .views import ( 
    PostLisView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView,
    PostDeleteView,
    UserPostLisView
    )
from .import views

#Path converters
urlpatterns = [
    path('', PostLisView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostLisView.as_view(), name='user-posts'),
    path('about/', views.about, name='blog-about'),
]