
from django.urls import path
from . import views

#Path converters
urlpatterns = [
    path('yurilima/', views.send_email_yuri_lima, name='yuri-lima'),
    path('portifolio/', views.YuriLimaPortifolio, name='yuri-lima-portifolio'),
]