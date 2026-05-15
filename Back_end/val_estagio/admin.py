from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario, Aluno, Secretaria


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):

    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
            )
        }),

        ('Informações pessoais', {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'unidade',
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'password1',
                'password2',
                'unidade',
            ),
        }),
    )

    list_display = (
        'username',
        'email',
        'unidade',
    )

    search_fields = (
        'username',
        'email',
    )

    ordering = ('username',)

    filter_horizontal = ()
    list_filter = ()


admin.site.register(Aluno)
admin.site.register(Secretaria)