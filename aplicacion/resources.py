from import_export import resources
from aplicacion.models import Hexagrama, Articulo

class HexagramaResource(resources.ModelResource):
    class Meta:
        model = Hexagrama
        

class ArticuloResource(resources.ModelResource):
    class Meta:
        model = Articulo
        