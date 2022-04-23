
from  django.urls import path, include
from .views import  index, elements, events, events_news, single_event, contact, buscar, Registro, CustomLoginView
from django.conf import settings
from django.conf.urls.static import static
from .froms import loginForm
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('', index, name='Inicio'),
    path('elements/', elements, name= 'Elementos'),
    path('events/', events, name= 'Eventos'),
    path('events_new', events_news, name='Eventos Nuevos'),
    path('single/', single_event, name= 'Single'),
    path('contact/', contact, name='Contactos'),
    path('buscar/', buscar, name='buscar'),
    path('registro/', Registro.as_view(), name='registro'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='app/login.html',authentication_form=loginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/logout.html'), name='logout'),
    
]
urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
