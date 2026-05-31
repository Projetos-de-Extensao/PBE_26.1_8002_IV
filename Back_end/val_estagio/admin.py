from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario, Aluno, Secretaria, Coordenador, Curso, Empresa, Tce, RelatorioSemestral, Estagio

class AlunoInline(admin.StackedInline):
    model = Aluno
    can_delete = False
    Extra = 0
    Fields = ('telefone', 'cpf', 'dt_nascimento', 'procurando_estagio', 'horas_estagio', 'periodo', 'curso')


class SecretariaInline(admin.StackedInline):
    model = Secretaria
    can_delete = False
    Extra = 0

class CoordenadorInline(admin.StackedInline):
    model = Coordenador
    can_delete = False
    Extra = 0
    Fields = ('area')

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):

    list_display = ['username', 'matricula', 'email', 'unidade', 'get_tipo']

    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {
            'fields': ('matricula', 'unidade',)
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações Adicionais', {
            'classes': ('wide',),
            'fields': ('matricula', 'unidade',),
        }),
    )

    inlines = [AlunoInline, SecretariaInline, CoordenadorInline]

    @admin.display(description='Tipo de Usuário')
    def get_tipo(self, obj):
        if hasattr(obj, 'aluno'):
            return 'Aluno'
        elif hasattr(obj, 'secretaria'):
            return 'Secretaria'
        elif hasattr(obj, 'coordenador'):
            return 'Coordenador'
        else:
            return 'Desconecido'



    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': (
    #             'username',
    #             'password1',
    #             'password2',
    #             'unidade',
    #         ),
    #     }),
    # )

    # search_fields = (
    #     'username',
    #     'email',
    # )

    # ordering = ('username',)

    # filter_horizontal = ()
    # list_filter = ()


# admin.site.register(Aluno)
# admin.site.register(Secretaria)
# admin.site.register(Coordenador)
# admin.site.register(Curso)
# admin.site.register(Empresa)
# admin.site.register(Tce)
# admin.site.register(RelatorioSemestral)
# admin.site.register(Estagio)