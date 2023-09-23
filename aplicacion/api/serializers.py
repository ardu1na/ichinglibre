from rest_framework import serializers
from aplicacion.models import Hexagrama, Tirada
from django.core.exceptions import ObjectDoesNotExist

        
class TiradaSerializer(serializers.ModelSerializer):
    h1 = serializers.SerializerMethodField()
    h2 = serializers.SerializerMethodField()

    mutables = serializers.SerializerMethodField()
    class Meta:
        model= Tirada
        fields = [
            'result',
            'h1',
            'mutables',
            'h2',
            
        ]
    
    def get_mutables(self, obj):
        mutable = {}
        if obj.mutable == False:
            mutable =  obj.mutable
        else:
            lineas = {}
            mutables = obj.lineas_mutables
            for mutable in mutables:
                if mutable == 1:
                    lineas['1'] = obj.h1.m1
                elif mutable == 2:
                    lineas['2'] = obj.h1.m2
                elif mutable == 3:
                    lineas['3'] = obj.h1.m3
                elif mutable == 4:
                    lineas['4'] = obj.h1.m4
                elif mutable == 5:
                    lineas['5'] = obj.h1.m5
                elif mutable == 6:
                    lineas['6'] = obj.h1.m6
                  
            mutable = {
                'es_mutable': obj.mutable,
                'mutables': lineas,
            }
        return mutable
        



    def get_h1(self, obj):
        try:
            articulo_texto = obj.h1.articulo.texto
        except ObjectDoesNotExist:
            articulo_texto = None
        h1 = {
            'nombre' : obj.h1.nombre,
            'numero': obj.h1.numero,
            'simbolo': obj.h1.simbolo,
            'lineas': obj.h1.lineas,
            'texto': obj.h1.texto,
        }
        return h1
    
    def get_h2(self, obj):
        if obj.mutable == True:
            h2 = {
                'nombre' : obj.h2.nombre,
                'numero': obj.h2.numero,
                'simbolo': obj.h2.simbolo,
                'lineas': obj.h2.lineas,
                'texto': obj.h2.texto,
            }
            return h2
        else:
            return None
    
    
class HexagramaSerializer(serializers.ModelSerializer):
   
    
    class Meta:
        model = Hexagrama
        fields = [
            'numero',
            'lineas',
            'nombre',
            'texto',
            'm1',
            'm1',
            'm1',
            'm1',
            'm1',
            'm1',
            'texto_expecial',
            'mas_info',
            'simbolo',
        ]