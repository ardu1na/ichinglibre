from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Hexagrama, Articulo

class HexagramaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Hexagrama.objects.all()
    
    def location(self, obj):
        return reverse('hexagrama') + '?busqueda={}'.format(obj.numero)



class ArticuloSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Articulo.objects.all()

    def location(self, obj):
        return reverse('articulo_detail', args=[obj.slug])
