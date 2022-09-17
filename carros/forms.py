from django.forms import ModelForm
from .models import Carros


class FormularioCarros(ModelForm):
    class Meta:
        model = Carros
        fields = ["marca", "modelo", "ano", "preco", "comentario"]
