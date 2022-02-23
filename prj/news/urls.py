from django.urls import path
from .views import default, news, detail

urlpatterns = [
    path('home/', default),
    path('news/', news, name='news'),
    path('news/<str:slug>', detail, name='detail'),
]