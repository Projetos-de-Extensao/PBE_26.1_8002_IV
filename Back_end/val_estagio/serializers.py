from rest_framework import serializers
from .models import Usuario, Aluno, Secretaria, Coordenador, Curso, Empresa, Seguradora, Tce, RelatorioSemestral, Estagio

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

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = 'id', 'nome', 'cnpj', 'endereco', 'telefone'
        read_only_fields = ['id']

class SeguradoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguradora
        fields = 'id', 'apolice_seguro', 'nome_seguradora'
        read_only_fields = ['id']

class TceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tce
        fields = 'id', 'aluno', 'seguradora', 'empresa_contratante', 'status'
        read_only_fields = ['id']

class RelatorioSemestralSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatorioSemestral
        fields = 'id', 'aluno', 'estagio', 'horas_estagiadas', 'em_aberto', 'semestre', 'data_envio', 'status'
        read_only_fields = ['id']

class EstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estagio
        fields = 'id', 'tce', 'empresa', 'aluno', 'data_inicio', 'data_fim', 'carga_horaria'
        read_only_fields = ['id']
        


        
