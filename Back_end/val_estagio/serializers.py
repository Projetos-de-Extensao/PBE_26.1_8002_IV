from rest_framework import serializers
from .models import Usuario, Aluno, Secretaria, Coordenador, Curso, Empresa, Seguradora, Tce, RelatorioSemestral, Estagio

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = 'id', 'username', 'email', 'first_name', 'last_name', 'unidade'
        read_only_fields = ['id']
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = 'id', 'nome'
        read_only_fields = ['id']

class AlunoSerializer(serializers.ModelSerializer):
    curso = CursoSerializer(read_only=True)
    class Meta:
        model = Aluno
        fields = 'id', 'usuario', 'matricula', 'cpf', 'dt_nascimento', 'procurando_estagio', 'horas_estagio', 'periodo', 'curso'
        read_only_fields = ['id']
class SecretariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secretaria
        fields = 'id', 'usuario', 'matricula_funcionario'
        read_only_fields = ['id']
class CoordenadorSerializer(serializers.ModelSerializer):
    cursos = CursoSerializer(read_only=True, many=True)
    class Meta:
        model = Coordenador
        fields = 'id', 'usuario', 'area', 'cursos'
        read_only_fields = ['id']

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = 'id', 'nome_empresa', 'cnpj', 'endereco_empresa'
        read_only_fields = ['id']

class SeguradoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguradora
        fields = 'id', 'apolice_seguro', 'nome_seguradora'
        read_only_fields = ['id']

class TceSerializer(serializers.ModelSerializer):
    empresa_nome = serializers.CharField(source='empresa_contratante.nome_empresa', read_only=True)
    aluno_nome = serializers.CharField(source='aluno.usuario.username', read_only=True)
    seguradora_nome = serializers.CharField(source='seguradora.nome_seguradora', read_only=True)

    class Meta:
        model = Tce
        fields = 'id', 'auxilio_bolsa', 'seguradora', 'seguradora_nome', 'aluno', 'aluno_nome', 'empresa_contratante', 'empresa_nome', 'data_inicio', 'data_fim', 'status'
        read_only_fields = ['id']

class RelatorioSemestralSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.CharField(source='aluno.usuario.username', read_only=True)
    empresa_nome = serializers.CharField(source='empresa_contratante.nome_empresa', read_only=True)
    class Meta:
        model = RelatorioSemestral
        fields = 'id', 'aluno', 'aluno_nome', 'empresa_nome', 'estagio', 'horas_estagiadas', 'em_aberto', 'semestre', 'data_envio', 'status'
        read_only_fields = ['id']

class EstagioSerializer(serializers.ModelSerializer):
    empresa_nome = serializers.CharField(source='empresa.nome_empresa', read_only=True)
    aluno_nome = serializers.CharField(source='aluno.usuario.username', read_only=True)
    class Meta:
        model = Estagio
        fields = 'id', 'tce', 'empresa', 'empresa_nome', 'aluno', 'aluno_nome', 'data_inicio', 'data_fim', 'carga_horaria'
        read_only_fields = ['id']




        
