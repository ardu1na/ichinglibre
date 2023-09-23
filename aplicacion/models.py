from datetime import date
import random
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

class Tirada(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="tiradas", on_delete=models.CASCADE, null=True, blank=True)
    
    result = models.JSONField(null=True, blank=True)
    
    especial = models.BooleanField(default=False)
    mutable = models.BooleanField(default=False)
    
    def __str__ (self):
        return f'{self.date.hour}:{self.date.minute} {self.date.day}/{self.date.month} consulta' 
    
    
    
    
        
    
    def save(self, *args, **kwargs):
        posibilidades = (1,2,3,4)
        tirada = random.choices(
                            posibilidades,
                            weights=(3,3,1,1),
                            k=6
                        )
        self.result = tirada
      

        
        if 3 in tirada or 4 in tirada:
            self.mutable = True

            
            
        super().save(*args, **kwargs) 
        
    @property
    def h1(self):
        tirada = self.result
        
        h1 = []

        for index, value in enumerate(tirada, start=1):
            if value == 3:
                h1.append(1)
            elif value == 4:
                h1.append(2)
            else:
                h1.append(value)
                
        try:
            h1 = Hexagrama.objects.get(lineas=h1)
            if h1:
                return h1
        except:
            return "no lo tenemos"
        
        
    @property
    def h2(self):
        if self.mutable == True:
            tirada = self.result
            
            h2 = []

            for index, value in enumerate(tirada, start=1):
                if value == 3:
                    h2.append(2)
                elif value == 4:
                    h2.append(1)
                else:
                    h2.append(value)
                    
            try:
                h2 = Hexagrama.objects.get(lineas=h2)
                if h2:
                    return h2
            except:
                return "no lo tenemos"
        else:
            return self.h1
        
    @property
    def lineas_mutables(self):
        tirada = self.result
        
        mutables = []

        for index, value in enumerate(tirada, start=1):
            if value == 3:
                mutables.append(index)
            elif value == 4:
                mutables.append(index)
        return mutables
        
            
            
class Hexagrama(models.Model):
    numero=models.IntegerField(unique=True)
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
