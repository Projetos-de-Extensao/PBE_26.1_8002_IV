from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Importa modelos (tabelas do banco de dados)
from .models import Usuario, Aluno, Secretaria, Coordenador, Curso, Empresa, Tce, RelatorioSemestral, Estagio

# Personalização do painel para o modelo de usuário customizado
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # Define os grupos de campos que aparecem na tela de edição de um usuário
    fieldsets = (
        (None, {
            'fields': ('username', 'password',)
        }),
        ('Informações pessoais', {
            'fields': ('first_name', 'last_name', 'email', 'unidade',)
        }),
    )

    # Define os campos necessários para a criação de um novo usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'unidade',),
        }),
    )

    # Colunas que aparecem na listagem principal no painel
    list_display = ('username', 'email', 'unidade',)

    # Habilita uma barra de busca no topo da lista
    search_fields = ('username', 'email',)

    # Define a ordenação padrão dos registros
    ordering = ('username',)

    # Configurações extras 
    filter_horizontal = ()
    list_filter = ()

# Registra os demais modelos para que apareçam no painel administrativo
# Sem isso, eles não apareceriam na interface do Admin
admin.site.register(Aluno)
admin.site.register(Secretaria)
admin.site.register(Coordenador)
admin.site.register(Curso)
admin.site.register(Empresa)
admin.site.register(Tce)
admin.site.register(RelatorioSemestral)
admin.site.register(Estagio)