from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from aplicacion.models import Hexagrama, Articulo, Tirada
from aplicacion.forms import ArticuloAdminForm
from aplicacion.resources import HexagramaResource, ArticuloResource

class HexagramaAdmin(ImportExportModelAdmin):
    list_display = ("numero", "nombre", "lineas")
    resource_class = HexagramaResource

admin.site.register(Hexagrama, HexagramaAdmin)
admin.site.register(Tirada)


class ArticuloAdmin(ImportExportModelAdmin):
    list_display = ("fecha", "titulo")
    form = ArticuloAdminForm
    resource_class = ArticuloResource

admin.site.register(Articulo, ArticuloAdmin)