
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

import random


from aplicacion.models import Hexagrama, Articulo

# Se llama a los gráficos asociados a cada linea
from aplicacion.lineas import *
from django.core.paginator import Paginator


from django.contrib.sitemaps import views as sitemap_views
from aplicacion.sitemaps import HexagramaSitemap, ArticuloSitemap

sitemaps = {
    'hexagramas': HexagramaSitemap,
    'articulos': ArticuloSitemap,
}

def sitemap(request, **kwargs):
    return sitemap_views.sitemap(request, sitemaps, **kwargs)




def blog(request):
    articulos = Articulo.objects.all().order_by('-id')
    paginator = Paginator(articulos, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context= {
        'articulos' : articulos,
    }
    return render(request, 'blog.html', context)



def articulo_detail(request, slug):
    articulo = get_object_or_404(Articulo, slug=slug)
    context = {'articulo': articulo}
    return render(request, 'articulo_detail.html', context)





# Formulario de búsqueda
def form(request):
    hexagramas = Hexagrama.objects.all()
    return render(request, 'iching/form.html', {'hexagramas':hexagramas})


# Resultado de la búsqueda
def hexagrama(request):
    if request.method != 'GET':
        return HttpResponse("Te hackeé")

    resultado = request.GET['busqueda']

    hexa = Hexagrama.objects.get(numero=resultado)

    # Gráfico para renderizar
    dibujohexa=[]
    for linea in hexa.lineas:
        if linea == 2:
            dibujohexa.append(yin)
        else:
            dibujohexa.append(yang)

    context = {
        'hexa' : hexa,
        'resultado' : resultado,
        'dibujohexa' : dibujohexa,
    }

    return render(request, 'iching/sucess.html', context)



def index(request):
    return render(request, 'index.html', {})

def contacto(request):
    return render(request, 'contacto/contacto.html', {})

def acercade(request):
    return render(request, 'iching/acercade.html', {})

def ayuda(request):
    return render(request, 'iching/ayuda.html', {})





# Lectura
def tirada(request):


    # generar lineas
    posibilidades = (1,2,3,4)
    tirada = random.choices(
                        posibilidades,
                        weights=(3,3,1,1),
                        k=6
                    )





    # Gráfico para renderizar
    dibujohexa1=[]
    for linea in tirada:
        if linea == 2:
            dibujohexa1.append(yin)
        elif linea == 4:
            dibujohexa1.append(myin)
        elif linea == 3:
            dibujohexa1.append(myang)
        else:
            dibujohexa1.append(yang)



    # buscar mutables y armar resultado
    mutables = []
    h1 = []
    h2 = []

    for index, value in enumerate(tirada, start=1):
        if value == 3:
            mutables.append(index)
            h1.append(1)
            h2.append(2)
        elif value == 4:
            mutables.append(index)
            h1.append(2)
            h2.append(1)
        else:
            h1.append(value)
            h2.append(value)


    # buscar primer hexagrama
    hexa1 = Hexagrama.objects.get(lineas=h1)

    # revisar si mutó
    if h1 == h2:
        es_mutable = False
    else:
        es_mutable = True

        # buscar el segundo hexagrama
        hexa2 = Hexagrama.objects.get(lineas=h2)

        # ver si es primario y mutan todas
        if hexa1.numero == 1 or hexa1.numero == 2 and len(mutables) == 6:
            es_especial = True
        else:
            es_especial = False




        dibujohexa2=[]
        for linea in h2:
            if linea == 2:
                dibujohexa2.append(yin)
            else:
                dibujohexa2.append(yang)



    if es_mutable == False:
        context = {
            'es_mutable': es_mutable,
            'hexa1': hexa1,
            'dibujohexa1': dibujohexa1

        }
    else:
        context = {
            'dibujohexa1': dibujohexa1,
            'dibujohexa2': dibujohexa2,
            'mutables': mutables,
            'es_mutable': es_mutable,
            'es_especial': es_especial,
            'hexa1': hexa1,
            'hexa2': hexa2,
        }

    return render(request, 'iching/tirada.html', context)