from rest_framework import serializers
from aplicacion.models import Hexagrama, Tirada

        
class TiradaSerializer(serializers.ModelSerializer):
    h1 = serializers.SerializerMethodField()
    
    class Meta:
        model= Tirada
        fields = [
            'result',
            'h1',
            
            
        ]
       
    def get_h1(self, obj):
        h1 = obj.h1
        return obj.h1.nombre
    
    
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