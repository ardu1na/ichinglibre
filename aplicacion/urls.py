from django.urls import path
from . import views
urlpatterns = [
    path('sitemap.xml', views.sitemap, name='django.contrib.sitemaps.views.sitemap'),

    path('', views.index, name="index"),
    path('tirada/', views.tirada, name='tirada'),
    path('contacto/', views.contacto, name='contacto'),
    path('acercade/', views.acercade, name='acercade'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('recursos/', views.form, name='form'),
    path('hexagrama/', views.hexagrama, name='hexagrama'), 
    path('articulos/', views.blog, name='blog'),
    path('<slug:slug>/', views.articulo_detail, name='articulo_detail'),
]

