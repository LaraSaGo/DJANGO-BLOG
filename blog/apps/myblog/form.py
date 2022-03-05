from .models import Comentarios, Post
from django import forms

class PostForm(forms.ModelForm,):
    class Meta:
        model = Post

        fields={
            'autor',
            'title',
            'texto',
        }

        labels={
            'autor':'Autor',
            'title':'Titulo',
            'texto':'Texto',

        }

class ComentariosForm(forms.ModelForm,):
    class Meta:
        model = Comentarios

        fields={
            'post',
            'autor',
            'text',
        }

        labels={
            'post':'Post',
            'autor':'Autor',
            'texto':'Texto',
        }