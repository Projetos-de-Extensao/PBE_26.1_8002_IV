from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario, Aluno, Secretaria, Coordenador, Curso, Empresa, Tce, RelatorioSemestral, Estagio

class AlunoInline(admin.StackedInline):
    model = Aluno
    can_delete = False
    extra = 0
    fields = ('telefone', 'cpf', 'dt_nascimento', 'procurando_estagio', 'horas_estagio', 'periodo', 'curso')


class SecretariaInline(admin.StackedInline):
    model = Secretaria
    can_delete = False
    extra = 0

class CoordenadorInline(admin.StackedInline):
    model = Coordenador
    can_delete = False
    extra = 0
    fields = ('area',)

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):

    list_display = ['username', 'first_name', 'last_name', 'matricula', 'email', 'unidade', 'get_tipo']

    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {
            'fields': ('matricula', 'unidade')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações Adicionais', {
            'classes': ('wide',),
            'fields': ('matricula', 'unidade', 'first_name', 'last_name', 'email'),
        }),
    )

    inlines = [AlunoInline, SecretariaInline, CoordenadorInline]

    @admin.display(description='Tipo de Usuário')
    def get_tipo(self, obj):
        if hasattr(obj, 'aluno'):
            return 'Aluno'
        elif hasattr(obj, 'coordenador'):
            return 'Coordenador'
        else:
            return 'Secretaria'
    
    
    filter_horizontal = ()
    
    list_filter = ('unidade', 'aluno__curso__nome', 'coordenador__area')

    ordering = ('username',)

    search_fields = (
        'matricula',
        'email',
    )



# admin.site.register(Curso)
# admin.site.register(Empresa)
# admin.site.register(Tce)
# admin.site.register(RelatorioSemestral)
# admin.site.register(Estagio)