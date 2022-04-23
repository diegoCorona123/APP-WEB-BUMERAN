
from django.shortcuts import render, redirect
from .models import empleo, Comentarios
from .froms import ComentariosForm, userForm, loginForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView

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
    comentarios = Comentarios.objects.all()
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

class Registro(View):
    form_class = userForm
    initial = {'key': 'value'}
    template_name = 'app/registro.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request, f'Account created for {username}')
             return redirect(to='/')
        return render(request, self.template_name, {'form': form})
    def dispatch(self, request, *args, **kwargs):
        # redirigirá a la página de inicio si un usuario intenta acceder a la página de registro mientras está conectado
        if request.user.is_authenticated:
             return redirect(to='/')
        return super(Registro, self).dispatch(request, *args, **kwargs)


class CustomLoginView(LoginView):
    form_class = loginForm
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            # set session expiry to  0 seconds. So it will automatically close the session after the browswe is closed.
            self.request.session.set_expiry(0)
            # set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True
        #else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


def buscar(request):
    if request.GET['busqueda']:
        query = request.GET ['busqueda']
        empleos = empleo.objects.filter(empleo=query).order_by('-descripcion')
        datos ={
        "empleos": empleos,
        "query": query
        }
        return render(request, 'app/buscar.html', datos)
    else:
        return render(request, 'app/buscar.html')



