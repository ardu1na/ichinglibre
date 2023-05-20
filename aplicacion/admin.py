from django.contrib import admin
from . models import Hexagrama, Articulo
from .forms import ArticuloAdminForm

class HexagramaAdmin(admin.ModelAdmin):
    list_display = ("numero", "nombre", "lineas")

admin.site.register(Hexagrama, HexagramaAdmin)


class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("fecha", "titulo")
    form=ArticuloAdminForm

admin.site.register(Articulo, ArticuloAdmin)