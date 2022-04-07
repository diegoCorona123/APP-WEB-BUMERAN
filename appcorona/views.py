from django.shortcuts import render
from .models import empleo
from .froms import ComentariosForm

# Create your views here.
def index(request):
    return render(request, 'app/index.html')
def elements(request):
    empleos = empleo.objects.all()
    datos = {
        "empleos": empleos   
    }
    return render(request,'app/elements.html', datos)
def events(request):
    return render(request, 'app/events.html')
def events_news(request):
    return render(request, 'app/events-news.html')
def single_event(request):
    return render(request, 'app/single-event.html')    
def contact(request):
    datos = {
        "from": ComentariosForm 
    }
    if request.method == 'POST':
        formulario = ComentariosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            datos["form"] = formulario
    return render(request,'app/contact.html', datos)
    
def buscar(request):
    if request.GET['busqueda']:
        query = request.GET ['busqueda']
        empleos = empleo.objects.filter(titulo=query).order_by('-descripcion')
        datos ={
            "empleo": empleo,
            "query": query
        }

        return render(request, 'app/busqueda.html', datos)
    else:
        return render(request, 'app/busqueda.html')



