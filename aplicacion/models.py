from datetime import date

from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Hexagrama(models.Model):
    numero=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50, null=False, blank= False)
    lineas=models.JSONField(null=False, blank=False, unique=True)
    texto=models.TextField(max_length=500, null=True, blank=True)
    m1=models.TextField(max_length=500, null=True, blank=True)
    m2=models.TextField(max_length=500, null=True, blank=True)
    m3=models.TextField(max_length=500, null=True, blank=True)
    m4=models.TextField(max_length=500, null=True, blank=True)
    m5=models.TextField(max_length=500, null=True, blank=True)
    m6=models.TextField(max_length=500, null=True, blank=True)
    texto_especial=models.TextField(max_length=500, null=True, blank=True)
    mas_info=models.URLField(null=True, blank=True)
    simbolo=models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.numero, self.nombre)

class Tag(models.Model):
    nombre=models.CharField(max_length=150, null=False, blank= False)
    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre=models.CharField(max_length=150, null=False, blank= False)

    def __str__(self):
        return self.nombre



class Articulo(models.Model):
    titulo=models.CharField(max_length=150, null=False, blank= False)
    texto=models.TextField(null=False, blank= False)
    descripcion=models.CharField(max_length=300, null=True, blank= True)
    fecha=models.DateField(null=True, blank=True, default=date.today)
    imagen=models.ImageField(null=True, blank=True)
    img_url=models.URLField(null=True, blank=True)
    slug=models.SlugField(null=True, blank=True, unique=True)
    tags = models.ManyToManyField(Tag, related_name="articulos", null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank= True, related_name="articulos")
    hexagrama = models.OneToOneField(Hexagrama, on_delete=models.SET_NULL, null=True, blank= True, related_name="articulo")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Articulo, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('articulo_detail', args=[str(self.slug)])

    class Meta:
        get_latest_by = "fecha"
        ordering = ["fecha",]
