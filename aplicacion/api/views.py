from rest_framework.views import APIView
from rest_framework.response import Response
from aplicacion.models import Tirada
from aplicacion.api.serializers import  TiradaSerializer

class TiradaAPIView(APIView):
    serializer_class = TiradaSerializer
    # TODO DELETE OLD 
    def get(self, request):
        queryset = Tirada.objects.create()
        serializer = self.serializer_class(queryset, many=False) 
        return Response(serializer.data)
    