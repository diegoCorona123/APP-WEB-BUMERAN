from django.contrib import admin
from .models import empleo 
from .models import Comentarios


# Register your models here.



class empleotAdmin(admin.ModelAdmin):
    list_display = ["titulo","ciudad","empresa"]
    list_editable= ["empresa"]
    search_fields = ["titulo", "descripcion"]
    list_filter = ["empleos_disponibles"]
    list_per_page = 3

admin.site.register(empleo, empleotAdmin)

admin.site.register(Comentarios)

