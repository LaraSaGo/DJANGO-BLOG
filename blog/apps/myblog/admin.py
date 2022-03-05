from django.contrib import admin
from django.db.models.lookups import PostgresOperatorLookup 
from .models import Post
from .models import Comentarios

# Register your models here.

admin.site.register(Post) 
admin.site.register(Comentarios)
