
from  django.urls import path, include
from .views import  index, elements, events, events_news, single_event,contact,buscar
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='Inicio'),
    path('elements/', elements, name= 'Elementos'),
    path('events/', events, name= 'Eventos'),
    path('events_new', events_news, name='Eventos Nuevos'),
    path('single/', single_event, name= 'Single'),
    path('contact/', contact, name='Contactos'),
    path('buscar/', buscar, name='buscar'),
    
]
urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
