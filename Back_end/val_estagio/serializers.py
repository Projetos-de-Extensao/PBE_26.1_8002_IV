from rest_framework import serializers
from .models import Usuario, Aluno, Secretaria, Coordenador, Curso, Empresa, Tce, RelatorioSemestral, Estagio

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = 'id', 'username', 'email', 'first_name', 'last_name', 'unidade', 'matricula'
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
        fields = 'id', 'usuario', 'area'
        read_only_fields = ['id']

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = 'id', 'nome_empresa', 'cnpj', 'cep', 'uf', 'cidade', 'log', 'num', 'comp', 'bairro' 
        read_only_fields = ['id']

class TceSerializer(serializers.ModelSerializer):

    aluno_nome = serializers.CharField(source='aluno.usuario.username', read_only=True)

    class Meta:
        model = Tce
        fields = 'id', 'bolsa', 'apoliceseguro', 'secretaria', 'aluno'
        read_only_fields = ['id']

class RelatorioSemestralSerializer(serializers.ModelSerializer):
    
    coordenador_nome = serializers.CharField(source='Coordenador.usuario.username', read_only=True)

    class Meta:
        model = RelatorioSemestral
        fields = 'idrelatorio', 'semestre', 'data_envio', 'estagio', 'horas_estagiadas', 'coordenador', 'status'
        read_only_fields = ['id']

class EstagioSerializer(serializers.ModelSerializer):
    empresa_nome = serializers.CharField(source='empresa.nome_empresa', read_only=True)

    class Meta:
        model = Estagio
        fields = 'idestagio', 'tce', 'empresa', 'empresa_nome', 'data_inicio', 'data_fim', 'cargahorariasemanal'
        read_only_fields = ['id']




        
