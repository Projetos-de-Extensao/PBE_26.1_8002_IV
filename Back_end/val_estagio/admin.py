from django.contrib import admin

from . models import Usuario, Aluno, Secretaria

admin.site.register(Usuario)
admin.site.register(Aluno)
admin.site.register(Secretaria)