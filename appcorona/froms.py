from django import forms
from .models import Comentarios

class ComentariosForm(forms .ModelForm):
    class Meta:
        model = Comentarios
        fields = ["nombre", "email", "motivo", "comentario"]
        #fields = '_all_'