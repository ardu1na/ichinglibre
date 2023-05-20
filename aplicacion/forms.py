from django import forms
from . models import Articulo

class ArticuloAdminForm(forms.ModelForm):
    texto= forms.CharField(widget=forms.Textarea(attrs={'id':"richtext_field"}))
    class Meta:
        model = Articulo
        fields = '__all__'