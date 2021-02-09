
from django.urls import path
from .views import ( 
    #Post
    PostLisView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView,
    PostDeleteView,
    UserPostLisView,

    #Painel
    PainelList,
    PainelCreate,
    PainelDetail,
    PainelUpdate,
    PainelDelete,
    UserPainelList
    )
from .import views

#Path converters
urlpatterns = [
    #Base Pages
    path('about/', views.about, name='blog-about'),

    #Post
    path('post/', PostLisView.as_view(), name='blog-home'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),    
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostLisView.as_view(), name='user-posts'),

    #Painel
    path('', PainelList.as_view(), name='painel-list'),
    path('painel/add/<int:pk>/', PainelCreate.as_view(), name='painel-add'),
    # path('painel/<int:pk>/',  PainelDetail.as_view(), name='painel-detail'),
    path('painel/<str:hashtag>/',  PainelDetail.as_view(), name='painel-detail'),
    path('painel/<int:pk>/update', PainelUpdate.as_view(), name='painel-update'),
    path('painel/<int:pk>/delete/', PainelDelete.as_view(), name='painel-delete'),

    path('userpainel/<str:username>', UserPainelList.as_view(), name='user-painel'),
]