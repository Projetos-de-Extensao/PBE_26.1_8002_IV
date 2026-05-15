from rest_framework import serializers
from .models import Usuario, Aluno, Secretaria, Coordenador, Curso

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = 'id', 'username', 'email', 'first_name', 'last_name', 'unidade'
        read_only_fields = ['id']
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = 'id', 'usuario', 'matricula', 'cpf', 'dt_nascimento', 'em_estagio', 'procurando_estagio', 'horas_estagio', 'periodo', 'curso'
        read_only_fields = ['id']
class SecretariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secretaria
        fields = 'id', 'usuario', 'matricula_funcionario'
        read_only_fields = ['id']
class CoordenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenador
        fields = 'id', 'usuario', 'cursos'
        read_only_fields = ['id']
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = 'id', 'nome', 'descricao'
        read_only_fields = ['id']


