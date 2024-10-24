from django.contrib import admin
from .models import Post, Comentario, Curtida

admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Curtida)