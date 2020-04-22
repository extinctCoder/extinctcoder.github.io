from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('projects/', views.projects, name='projects'),
    path('about_me/', views.about_me, name='about_me'),
]
